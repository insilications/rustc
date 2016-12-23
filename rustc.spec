Name     : rustc
Version  : 1.14.0
Release  : 17
URL      : https://static.rust-lang.org/dist/rust-1.14.0-x86_64-unknown-linux-gnu.tar.gz
Source0  : https://static.rust-lang.org/dist/rust-1.14.0-x86_64-unknown-linux-gnu.tar.gz
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
Provides: librustc_driver-f5a209a9.so()(64bit)
Provides: librustdoc-f5a209a9.so()(64bit)
Provides: libstd-f5a209a9.so()(64bit)

%description lib
Rust compiler

%prep
%setup -q -n rust-1.14.0-x86_64-unknown-linux-gnu

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/bash-completion/completions
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_datadir}/zsh/site-functions
install -d %{buildroot}%{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib
install -d %{buildroot}%{_prefix}/lib
install cargo/bin/cargo %{buildroot}%{_bindir}/
install cargo/etc/bash_completion.d/cargo %{buildroot}%{_datadir}/bash-completion/completions/
install cargo/share/man/man1/cargo.1 %{buildroot}%{_mandir}/man1/
install cargo/share/zsh/site-functions/_cargo %{buildroot}%{_datadir}/zsh/site-functions/
install rustc/bin/rust-gdb %{buildroot}%{_bindir}/
install rustc/bin/rustc %{buildroot}%{_bindir}/
install rustc/bin/rustdoc %{buildroot}%{_bindir}/
install rustc/share/man/man1/rustc.1 %{buildroot}%{_mandir}/man1/
install rustc/share/man/man1/rustdoc.1 %{buildroot}%{_mandir}/man1/
# Location is for rust-gdb to set path of python scripts
cp -a rustc/lib/rustlib %{buildroot}%{_prefix}/lib/
cp -a rustc/lib/*.so %{buildroot}%{_libdir}/
cp -a rust-std-x86_64-unknown-linux-gnu/lib/rustlib/x86_64-unknown-linux-gnu/lib/* %{buildroot}%{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/

%files
%defattr(-,root,root,-)
%exclude %{_prefix}/lib/rustlib/etc/*.pyo
%exclude %{_prefix}/lib/rustlib/etc/*.pyc

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
%{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/*.rlib
%{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/*.so
%{_prefix}/lib/rustlib/etc/*.py
