Name     : rustc
Version  : 1.4.0
Release  : 6
URL      : https://static.rust-lang.org/dist/rust-1.4.0-x86_64-unknown-linux-gnu.tar.gz
Source0  : https://static.rust-lang.org/dist/rust-1.4.0-x86_64-unknown-linux-gnu.tar.gz
Summary  : Rust compiler
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause GPL-3.0 ISC MIT NCSA
Requires : rustc-bin
Requires : rustc-data
Requires : rustc-doc
Requires : rustc-lib

%description
Rust compiler

%package bin
Summary: Rust compiler
Group: Binaries
Requires: rustc-lib
Requires: rustc-data

%description bin
Rust compiler

%package data
Summary: Rust compiler
Group: Data

%description data
Rust compiler

%package doc
Summary: Rust compiler
Group: Documentation

%description doc
Rust compiler

%package lib
Summary: Rust compiler
Group: Libraries%
Provides: librustc_driver-1bf6e69c.so()(64bit)
Provides: librustdoc-1bf6e69c.so()(64bit)
Provides: libstd-1bf6e69c.so()(64bit)

%description lib
Rust compiler

%prep
%setup -q -n rust-1.4.0-x86_64-unknown-linux-gnu

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}
install -d %{buildroot}%{_datadir}/bash-completion/completions
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_datadir}/zsh/site-functions
install -d %{buildroot}%{_libdir}
install cargo/bin/cargo %{buildroot}%{_bindir}/
install cargo/etc/bash_completion.d/cargo %{buildroot}%{_datadir}/bash-completion/completions/
install cargo/share/man/man1/cargo.1 %{buildroot}%{_mandir}/man1/
install cargo/share/zsh/site-functions/_cargo %{buildroot}%{_datadir}/zsh/site-functions/
install rustc/bin/rust-gdb %{buildroot}%{_bindir}/
install rustc/bin/rustc %{buildroot}%{_bindir}/
install rustc/bin/rustdoc %{buildroot}%{_bindir}/
install rustc/share/man/man1/rustc.1 %{buildroot}%{_mandir}/man1/
install rustc/share/man/man1/rustdoc.1 %{buildroot}%{_mandir}/man1/
cp -a rustc/lib/rustlib %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libarena-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libflate-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libfmt_macros-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libgetopts-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libgraphviz-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/liblog-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librbml-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_back-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_borrowck-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_data_structures-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_driver-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_lint-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_llvm-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_privacy-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_resolve-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_trans-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_typeck-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustdoc-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libserialize-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libstd-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libsyntax-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libterm-1bf6e69c.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libtest-1bf6e69c.so %{buildroot}%{_libdir}/

%files
%defattr(-,root,root,-)
%exclude %{_libdir}/rustlib/etc/*.pyc
%exclude %{_libdir}/rustlib/etc/*.pyo

%files bin
%defattr(-,root,root,-)
%{_bindir}/*

%files data
%defattr(-,root,root,-)
%{_datadir}/bash-completion/completions/cargo
%{_datadir}/zsh/site-functions/_cargo

%files doc
%defattr(-,root,root,-)
%{_mandir}/man1/*.1

%files lib
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/rustlib/etc/*.py
%{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/*.a
%{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/*.rlib
%{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/*.so
