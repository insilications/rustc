%global rust_triple x86_64-unknown-linux-gnu

# To bootstrap from scratch, set the channel and date from src/stage0.txt
# e.g. 1.10.0 wants rustc: 1.9.0-2016-05-24
# or nightly wants some beta-YYYY-MM-DD
%global bootstrap_rust 1.16.0
%global bootstrap_cargo 0.16.0
%global bootstrap_channel %{bootstrap_rust}
%global bootstrap_date 2017-03-11

Name:           rustc
Version:        1.17.0
Release:        20
Summary:        The Rust Programming Language
License:        Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT
URL:            https://www.rust-lang.org
Source0:        https://static.rust-lang.org/dist/rustc-1.17.0-src.tar.gz

# Bootstrap
# Add an additional binary Source.
Source1: https://static.rust-lang.org/dist/2017-03-11/rust-1.16.0-x86_64-unknown-linux-gnu.tar.gz

# Bootstrap
%global bootstrap_root rust-%{bootstrap_channel}-%{rust_triple}
%global local_rust_root %{_builddir}/%{bootstrap_root}%{_prefix}
Provides:       bundled(%{name}-bootstrap) = %{bootstrap_rust}
# No Bootstrap
# BuildRequires:  cargo >= %{bootstrap_cargo}
# BuildRequires:  %{name} >= %{bootstrap_rust}
# BuildConflicts: %{name} > %{version}
# ?global local_rust_root %{_prefix}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-dev
BuildRequires:  zlib-dev
BuildRequires:  python
BuildRequires:  curl

BuildRequires:  llvm-dev >= 3.7

# make check needs "ps" for src/test/run-pass/wait-forked-but-failed-child.rs
BuildRequires:  procps-ng

# debuginfo-gdb tests need gdb
BuildRequires:  gdb

# TODO: work on unbundling these!
Provides:       bundled(hoedown) = 3.0.5
Provides:       bundled(jquery) = 2.1.4
Provides:       bundled(libbacktrace) = 6.1.0
Provides:       bundled(miniz) = 1.14

# The C compiler is needed at runtime just for linking.  Someday rustc might
# invoke the linker directly, and then we'll only need binutils.
# https://github.com/rust-lang/rust/issues/11937
Requires:       gcc

# ALL Rust libraries are private, because they don't keep an ABI.
%global _privatelibs lib.*-[[:xdigit:]]*[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

# While we don't want to encourage dynamic linking to Rust shared libraries, as
# there's no stable ABI, we still need the unallocated metadata (.rustc) to
# support custom-derive plugins like #[proc_macro_derive(Foo)].  But eu-strip is
# very eager by default, so we have to limit it to -g, only debugging symbols.
%global _find_debuginfo_opts -g

# Use hardening ldflags.
%global rustflags -Clink-arg=-Wl,-z,relro,-z,now

%description
Rust is a systems programming language that runs blazingly fast, prevents
segfaults, and guarantees thread safety.

%prep

# Bootstrap
%setup -q -n %{bootstrap_root} -T -b 1
./install.sh --components=cargo,rustc,rust-std-%{rust_triple} \
  --prefix=./%{_prefix} --disable-ldconfig
test -f %{local_rust_root}/bin/cargo
test -f %{local_rust_root}/bin/rustc

%setup -q -n rustc-1.17.0-src

# unbundle
rm -rf src/jemalloc/
rm -rf src/llvm/

# extract bundled licenses for packaging
cp src/rt/hoedown/LICENSE src/rt/hoedown/LICENSE-hoedown
sed -e '/*\//q' src/libbacktrace/backtrace.h \
  >src/libbacktrace/LICENSE-libbacktrace

# These tests assume that alloc_jemalloc is present
# https://github.com/rust-lang/rust/issues/35017
sed -i.jemalloc -e '1i // ignore-test jemalloc is disabled' \
  src/test/compile-fail/allocator-dylib-is-system.rs \
  src/test/compile-fail/allocator-rust-dylib-is-jemalloc.rs \
  src/test/run-pass/allocator-default.rs

#%patch1 -p1 -b .no-override


%build

%{?cmake_path:export PATH=%{cmake_path}:$PATH}
export RUSTFLAGS="%{rustflags}"

# We're going to override --libdir when configuring to get rustlib into a
# common path, but we'll fix the shared libraries during install.
%global common_libdir /usr/lib
%global rustlibdir %{common_libdir}/rustlib

%configure --disable-option-checking \
  --libdir=%{common_libdir} \
  --build=%{rust_triple} --host=%{rust_triple} --target=%{rust_triple} \
  --enable-local-rust --local-rust-root=%{local_rust_root} \
  --llvm-root=/usr --disable-codegen-tests \
  --enable-llvm-link-shared \
  --disable-jemalloc \
  --disable-rpath \
  --enable-debuginfo \
  --enable-vendor \
  --release-channel=stable

./x.py dist


%install
%{?cmake_path:export PATH=%{cmake_path}:$PATH}
export RUSTFLAGS="%{rustflags}"

DESTDIR=%{buildroot} ./x.py dist --install

# The libdir libraries are identical to those under rustlib/, and we need
# the latter in place to support dynamic linking for compiler plugins, so we'll
# point ldconfig to rustlib/ and remove the former.
# ?global rust_ldconfig %{_sysconfdir}/ld.so.conf.d/rust-%{_arch}.conf
# mkdir -p %{buildroot}$(dirname %{rust_ldconfig})
# echo "%{rustlibdir}/%{rust_triple}/lib" > %{buildroot}%{rust_ldconfig}
# rm -v %{buildroot}%{common_libdir}/*.so

# Remove installer artifacts (manifests, uninstall scripts, etc.)
find %{buildroot}%{rustlibdir} -maxdepth 1 -type f -exec rm -v '{}' '+'

# The shared libraries should be executable for debuginfo extraction.
find %{buildroot}%{rustlibdir}/ -type f -name '*.so' -exec chmod -v +x '{}' '+'

# FIXME: __os_install_post will strip the rlibs
# -- should we find a way to preserve debuginfo?

# Remove unwanted documentation files
rm -fr %{buildroot}%{_docdir}

%check
%{?cmake_path:export PATH=%{cmake_path}:$PATH}
export RUSTFLAGS="%{rustflags}"

# The results are not stable on koji, so mask errors and just log it.
./x.py test || :

%files
/usr/bin/rust-gdb
/usr/bin/rust-lldb
/usr/bin/rustc
/usr/bin/rustdoc
/usr/lib/*.so
/usr/lib/rustlib/etc/*.py
%exclude /usr/lib/rustlib/etc/*.pyc
%exclude /usr/lib/rustlib/etc/*.pyo
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/*.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/*.so
/usr/share/man/man1/rustc.1
/usr/share/man/man1/rustdoc.1
