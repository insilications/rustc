Name:           rustc
Version:        1.27.1
Release:        47
Summary:        The Rust Programming Language
License:        Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT
URL:            https://www.rust-lang.org
Source0:        https://static.rust-lang.org/dist/rustc-1.27.1-src.tar.gz
Patch1:         0001-Ensure-libs-built-in-stage0-have-unique-metadat.patch
Patch2:         0002-Fix-new-renamed_and_removed_lints-warning-247.patch
AutoReqProv:    No

BuildRequires:  cargo >= 0.18.0
BuildRequires:  rustc >= 0.17.0
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-dev
BuildRequires:  ncurses-dev
BuildRequires:  zlib-dev
BuildRequires:  python3
BuildRequires:  curl
BuildRequires:  llvm-dev >= 3.7

# make check needs "ps" for src/test/run-pass/wait-forked-but-failed-child.rs
BuildRequires:  procps-ng

# debuginfo-gdb tests need gdb
BuildRequires:  gdb

# TODO: work on unbundling these!
Provides:       bundled(libbacktrace) = 6.1.0
Provides:       bundled(miniz) = 1.16beta+r1

Requires:       binutils
Requires:       gcc
Requires:       gcc-dev
Requires:       libc6-dev
Requires:       llvm


%description
Rust is a systems programming language that runs blazingly fast, prevents
segfaults, and guarantees thread safety.

%prep

%setup -q -n rustc-%{version}-src
%patch1 -p1
pushd src/vendor/error-chain
%patch2 -p1
popd

%build
%configure \
    --build=x86_64-unknown-linux-gnu \
    --host=x86_64-unknown-linux-gnu \
    --target=x86_64-unknown-linux-gnu \
    --disable-option-checking \
    --libdir=/usr/lib \
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

# The configure macro will modify some autoconf-related files, which upsets
# cargo when it tries to verify checksums in those files.  If we just truncate
# that file list, cargo won't have anything to complain about.
find src/vendor -name .cargo-checksum.json \
     -exec sed -i.uncheck -e 's/"files":{[^}]*}/"files":{ }/' '{}' '+'

python3 x.py build

%install
export RUSTFLAGS="-Clink-arg=-Wl,-z,relro,-z,now"

DESTDIR=%{buildroot} python3 x.py install

# # Remove installer artifacts (manifests, uninstall scripts, etc.)
find %{buildroot}/usr/lib/rustlib -maxdepth 1 -type f -exec rm -v '{}' '+'

# # The shared libraries should be executable for debuginfo extraction.
find %{buildroot}/usr/lib/rustlib/ -type f -name '*.so' -exec chmod -v +x '{}' '+'

# # FIXME: __os_install_post will strip the rlibs
# # -- should we find a way to preserve debuginfo?

# # Remove unwanted documentation files
rm -fr %{buildroot}/usr/share/doc
mkdir -p %{buildroot}/usr/lib64
mv %{buildroot}/usr/lib/*.so %{buildroot}/usr/lib64
mkdir -p %{buildroot}/usr/lib64/rustlib
mv %{buildroot}/usr/lib/rustlib/x86_64-unknown-linux-gnu %{buildroot}/usr/lib64/rustlib

%files
/usr/bin/rust-gdb
/usr/bin/rust-lldb
/usr/bin/rustc
/usr/bin/rustdoc
/usr/lib64/*.so
/usr/lib/rustlib/etc/*.py
/usr/lib64/rustlib/x86_64-unknown-linux-gnu/lib/*.rlib
/usr/lib64/rustlib/x86_64-unknown-linux-gnu/lib/*.so
/usr/lib64/rustlib/x86_64-unknown-linux-gnu/codegen-backends/*.so
/usr/share/man/man1/rustc.1
/usr/share/man/man1/rustdoc.1
