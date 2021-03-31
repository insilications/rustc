#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : rustc
Version  : 64.unknown.gnu
Release  : 84
URL      : https://static.rust-lang.org/dist/rust-nightly-x86_64-unknown-linux-gnu.tar.gz
Source0  : https://static.rust-lang.org/dist/rust-nightly-x86_64-unknown-linux-gnu.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: rustc-bin = %{version}-%{release}
Requires: rustc-data = %{version}-%{release}
Requires: rustc-libexec = %{version}-%{release}
Requires: rustc-man = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
# Ignore missing build ids
%undefine _missing_build_ids_terminate_build
# Disable automatic requeriments processing
AutoReq: no

%description
# The Rust Programming Language
This is the main source code repository for [Rust]. It contains the compiler,
standard library, and documentation.

%package bin
Summary: bin components for the rustc package.
Group: Binaries
Requires: rustc-data = %{version}-%{release}
Requires: rustc-libexec = %{version}-%{release}
# Disable automatic requeriments processing
AutoReq: no

%description bin
bin components for the rustc package.


%package data
Summary: data components for the rustc package.
Group: Data
# Disable automatic requeriments processing
AutoReq: no

%description data
data components for the rustc package.


%package dev
Summary: dev components for the rustc package.
Group: Development
Requires: rustc-bin = %{version}-%{release}
Requires: rustc-data = %{version}-%{release}
Provides: rustc-devel = %{version}-%{release}
Requires: rustc = %{version}-%{release}
# Disable automatic requeriments processing
AutoReq: no

%description dev
dev components for the rustc package.


%package doc
Summary: doc components for the rustc package.
Group: Documentation
Requires: rustc-man = %{version}-%{release}
# Disable automatic requeriments processing
AutoReq: no

%description doc
doc components for the rustc package.


%package libexec
Summary: libexec components for the rustc package.
Group: Default
# Disable automatic requeriments processing
AutoReq: no

%description libexec
libexec components for the rustc package.


%package man
Summary: man components for the rustc package.
Group: Default
# Disable automatic requeriments processing
AutoReq: no

%description man
man components for the rustc package.


%package staticdev
Summary: staticdev components for the rustc package.
Group: Default
Requires: rustc-dev = %{version}-%{release}
# Disable automatic requeriments processing
AutoReq: no

%description staticdev
staticdev components for the rustc package.


%prep
%setup -q -n rust-nightly-x86_64-unknown-linux-gnu
cd %{_builddir}/rust-nightly-x86_64-unknown-linux-gnu

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617233346
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC"
#
export FCFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export FFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export CFFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export LDFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
#
# export PATH="/usr/lib64/ccache/bin:$PATH"
# export CCACHE_NOHASHDIR=1
# export CCACHE_DIRECT=1
# export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
## altflags1 end
echo "Installing..."


%install
export SOURCE_DATE_EPOCH=1617233346
rm -rf %{buildroot}
## install_macro start
./install.sh --prefix=%{?buildroot:%{buildroot}}/usr/ --libdir=%{?buildroot:%{buildroot}}/usr/lib/ --disable-ldconfig --without=rust-docs --verbose
install -dm 0755 %{buildroot}/usr/share/bash-completion/completions
install -m0644  %{buildroot}/usr/etc/bash_completion.d/cargo %{buildroot}/usr/share/bash-completion/completions/cargo
rm -rf %{buildroot}/usr/etc/bash_completion.d/cargo
find %{?buildroot:%{buildroot}} -name "install.log" -exec rm {} \;
find %{?buildroot:%{buildroot}} -type f -name '*manifest-*' -exec sed -i 's/\/builddir\/build\/BUILDROOT\/rustc-[0-9]*\.unknown\.gnu-[0-9]*\.x86_64//g' {} \;
## install_macro end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cargo
/usr/bin/cargo-clippy
/usr/bin/cargo-miri
/usr/bin/clippy-driver
/usr/bin/miri
/usr/bin/rust-analyzer
/usr/bin/rust-gdb
/usr/bin/rust-gdbgui
/usr/bin/rust-lldb
/usr/bin/rustc
/usr/bin/rustdoc
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/llc
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-ar
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-as
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-cov
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-dis
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-nm
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-objcopy
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-objdump
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-profdata
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-readobj
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-size
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/llvm-strip
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/opt
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/rust-lld
/usr/lib/rustlib/x86_64-unknown-linux-gnu/bin/rust-llvm-dwp

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/cargo
/usr/share/zsh/site-functions/_cargo

%files dev
%defattr(-,root,root,-)
/usr/lib/libLLVM-12-rust-1.53.0-nightly.so
/usr/lib/librustc_driver-be6d6107389669b3.so
/usr/lib/libstd-61556e43b375c2c0.so
/usr/lib/libtest-a3b2353c72e89634.so
/usr/lib/rustlib/components
/usr/lib/rustlib/etc/gdb_load_rust_pretty_printers.py
/usr/lib/rustlib/etc/gdb_lookup.py
/usr/lib/rustlib/etc/gdb_providers.py
/usr/lib/rustlib/etc/lldb_commands
/usr/lib/rustlib/etc/lldb_lookup.py
/usr/lib/rustlib/etc/lldb_providers.py
/usr/lib/rustlib/etc/rust_types.py
/usr/lib/rustlib/manifest-cargo
/usr/lib/rustlib/manifest-clippy-preview
/usr/lib/rustlib/manifest-llvm-tools-preview
/usr/lib/rustlib/manifest-miri-preview
/usr/lib/rustlib/manifest-rust-analysis-x86_64-unknown-linux-gnu
/usr/lib/rustlib/manifest-rust-analyzer-preview
/usr/lib/rustlib/manifest-rust-std-x86_64-unknown-linux-gnu
/usr/lib/rustlib/manifest-rustc
/usr/lib/rustlib/rust-installer-version
/usr/lib/rustlib/uninstall.sh
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libaddr2line-073b1b693304b876.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libadler-4b7dae8949ac132c.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/liballoc-3aeb407930ebd519.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libcfg_if-022f1a0e7cd794ec.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libcompiler_builtins-761b290f47712921.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libcore-166dae07beec0398.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libgetopts-ba1c7bc534f87985.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libgimli-c07f996a53ee6558.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libhashbrown-978dd04958b6ebcc.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/liblibc-ff456575f1773ef0.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libminiz_oxide-dda4c0b69607e93b.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libobject-978e97832b309706.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libpanic_abort-17bb75147d2bbed4.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libpanic_unwind-787faa8b02fbd963.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libproc_macro-5d1162e60f7751bc.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libprofiler_builtins-d7ef95407de55144.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/librustc_demangle-0ae8ed6a282247d0.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/librustc_std_workspace_alloc-14b94bdd9a47d665.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/librustc_std_workspace_core-6ab1ee6dbc17ad08.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/librustc_std_workspace_std-716101092d4b23f1.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libstd-61556e43b375c2c0.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libterm-a76a7ffc0867499d.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libtest-a3b2353c72e89634.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libunicode_width-d0a3572205759673.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/analysis/libunwind-bff7534e4dfcef6c.json
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libLLVM-12-rust-1.53.0-nightly.so
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libaddr2line-073b1b693304b876.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libadler-4b7dae8949ac132c.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/liballoc-3aeb407930ebd519.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcfg_if-022f1a0e7cd794ec.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcompiler_builtins-761b290f47712921.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcore-166dae07beec0398.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libgetopts-ba1c7bc534f87985.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libgimli-c07f996a53ee6558.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libhashbrown-978dd04958b6ebcc.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/liblibc-ff456575f1773ef0.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libminiz_oxide-dda4c0b69607e93b.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libobject-978e97832b309706.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libpanic_abort-17bb75147d2bbed4.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libpanic_unwind-787faa8b02fbd963.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libproc_macro-5d1162e60f7751bc.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libprofiler_builtins-d7ef95407de55144.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_demangle-0ae8ed6a282247d0.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_std_workspace_alloc-14b94bdd9a47d665.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_std_workspace_core-6ab1ee6dbc17ad08.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_std_workspace_std-716101092d4b23f1.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libstd-61556e43b375c2c0.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libstd-61556e43b375c2c0.so
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libterm-a76a7ffc0867499d.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libtest-a3b2353c72e89634.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libtest-a3b2353c72e89634.so
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libunicode_width-d0a3572205759673.rlib
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libunwind-bff7534e4dfcef6c.rlib

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/cargo/LICENSE-APACHE
/usr/share/doc/cargo/LICENSE-MIT
/usr/share/doc/cargo/LICENSE-THIRD-PARTY
/usr/share/doc/cargo/README.md
/usr/share/doc/clippy/LICENSE-APACHE
/usr/share/doc/clippy/LICENSE-MIT
/usr/share/doc/clippy/README.md
/usr/share/doc/miri/LICENSE-APACHE
/usr/share/doc/miri/LICENSE-MIT
/usr/share/doc/miri/README.md
/usr/share/doc/rust-analyzer/LICENSE-APACHE
/usr/share/doc/rust-analyzer/LICENSE-MIT
/usr/share/doc/rust-analyzer/README.md
/usr/share/doc/rust/COPYRIGHT
/usr/share/doc/rust/LICENSE-APACHE
/usr/share/doc/rust/LICENSE-MIT
/usr/share/doc/rust/README.md

%files libexec
%defattr(-,root,root,-)
/usr/libexec/cargo-credential-1password

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cargo-bench.1
/usr/share/man/man1/cargo-build.1
/usr/share/man/man1/cargo-check.1
/usr/share/man/man1/cargo-clean.1
/usr/share/man/man1/cargo-doc.1
/usr/share/man/man1/cargo-fetch.1
/usr/share/man/man1/cargo-fix.1
/usr/share/man/man1/cargo-generate-lockfile.1
/usr/share/man/man1/cargo-help.1
/usr/share/man/man1/cargo-init.1
/usr/share/man/man1/cargo-install.1
/usr/share/man/man1/cargo-locate-project.1
/usr/share/man/man1/cargo-login.1
/usr/share/man/man1/cargo-metadata.1
/usr/share/man/man1/cargo-new.1
/usr/share/man/man1/cargo-owner.1
/usr/share/man/man1/cargo-package.1
/usr/share/man/man1/cargo-pkgid.1
/usr/share/man/man1/cargo-publish.1
/usr/share/man/man1/cargo-run.1
/usr/share/man/man1/cargo-rustc.1
/usr/share/man/man1/cargo-rustdoc.1
/usr/share/man/man1/cargo-search.1
/usr/share/man/man1/cargo-test.1
/usr/share/man/man1/cargo-tree.1
/usr/share/man/man1/cargo-uninstall.1
/usr/share/man/man1/cargo-update.1
/usr/share/man/man1/cargo-vendor.1
/usr/share/man/man1/cargo-verify-project.1
/usr/share/man/man1/cargo-version.1
/usr/share/man/man1/cargo-yank.1
/usr/share/man/man1/cargo.1
/usr/share/man/man1/rustc.1
/usr/share/man/man1/rustdoc.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc-nightly_rt.asan.a
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc-nightly_rt.lsan.a
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc-nightly_rt.msan.a
/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc-nightly_rt.tsan.a
