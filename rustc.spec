%global rust_triple x86_64-unknown-linux-gnu

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

Name:           rustc
Version:        1.20.0
Release:        30
Summary:        The Rust Programming Language
License:        Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT
URL:            https://www.rust-lang.org
Source0:        https://static.rust-lang.org/dist/rustc-1.20.0-src.tar.gz
Patch1:         0001-Update-stage0-sysroot-incremental-lib-directory.patch

BuildRequires:  cargo >= 0.18.0
BuildRequires:  %{name} >= 0.17.0
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-dev
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

Requires:       binutils
Requires:       gcc
Requires:       gcc-dev
Requires:       libc6-dev


%description
Rust is a systems programming language that runs blazingly fast, prevents
segfaults, and guarantees thread safety.

%prep

%setup -q -n rustc-%{version}-src

%patch1 -p1

# unbundle
rm -rf src/llvm/

%build
export RUSTFLAGS="%{rustflags}"

# We're going to override --libdir when configuring to get rustlib into a
# common path, but we'll fix the shared libraries during install.
%configure \
    --build=%{rust_triple} \
    --host=%{rust_triple} \
    --target=%{rust_triple} \
    --disable-option-checking \
    --libdir=/usr/lib64 \
    --enable-local-rust \
    --local-rust-root=/usr \
    --llvm-root=/usr \
    --disable-codegen-tests \
    --enable-llvm-link-shared \
    --disable-jemalloc \
    --disable-rpath \
    --enable-debuginfo \
    --enable-vendor \
    --release-channel=stable

./x.py build

%install
export RUSTFLAGS="%{rustflags}"

DESTDIR=%{buildroot} ./x.py install

# Remove installer artifacts (manifests, uninstall scripts, etc.)
find %{buildroot}/usr/lib64/rustlib -maxdepth 1 -type f -exec rm -v '{}' '+'

# The shared libraries should be executable for debuginfo extraction.
find %{buildroot}/usr/lib64/rustlib/ -type f -name '*.so' -exec chmod -v +x '{}' '+'

# FIXME: __os_install_post will strip the rlibs
# -- should we find a way to preserve debuginfo?

# Remove unwanted documentation files
rm -fr %{buildroot}/usr/share/doc

%files
/usr/bin/rust-gdb
/usr/bin/rust-lldb
/usr/bin/rustc
/usr/bin/rustdoc
/usr/lib64/*.so
/usr/lib64/rustlib/etc/*.py
%exclude /usr/lib64/rustlib/etc/*.pyc
%exclude /usr/lib64/rustlib/etc/*.pyo
/usr/lib64/rustlib/x86_64-unknown-linux-gnu/lib/*.rlib
/usr/lib64/rustlib/x86_64-unknown-linux-gnu/lib/*.so
/usr/share/man/man1/rustc.1
/usr/share/man/man1/rustdoc.1
