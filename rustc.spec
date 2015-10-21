Name     : rustc
Version  : 1.3.0
Release  : 3
URL      : https://static.rust-lang.org/dist/rust-1.3.0-x86_64-unknown-linux-gnu.tar.gz
Source0  : https://static.rust-lang.org/dist/rust-1.3.0-x86_64-unknown-linux-gnu.tar.gz
Summary  : Rust compiler
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause GPL-3.0 ISC MIT NCSA
Provides : librustc_driver-198068b3
Provides : librustdoc-198068b3
Provides : libstd-198068b3



%description
Rust compiler

%prep
%setup -q -n rust-1.3.0-x86_64-unknown-linux-gnu

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
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libarena-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libflate-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libfmt_macros-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libgetopts-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libgraphviz-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/liblog-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librbml-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_back-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_borrowck-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_data_structures-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_driver-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_lint-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_llvm-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_privacy-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_resolve-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_trans-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustc_typeck-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/librustdoc-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libserialize-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libstd-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libsyntax-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libterm-198068b3.so %{buildroot}%{_libdir}/
ln -s %{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/libtest-198068b3.so %{buildroot}%{_libdir}/

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/bash-completion/completions/cargo
%{_datadir}/zsh/site-functions/_cargo
%{_libdir}/*.so
%{_libdir}/rustlib/etc/*.py
%exclude %{_libdir}/rustlib/etc/*.pyc
%exclude %{_libdir}/rustlib/etc/*.pyo
%{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/*.a
%{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/*.rlib
%{_libdir}/rustlib/x86_64-unknown-linux-gnu/lib/*.so
%{_mandir}/man1/*.1
