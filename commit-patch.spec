Name: commit-patch
Version: 2.2
Release: %mkrel 1
Summary: A utility that lets you check select portions of a file into a VCS
License: GPLv2
URL: http://porkrind.org/commit-patch/
Group: Text tools
Source: http://porkrind.org/commit-patch/commit-patch-2.2.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch

%description
Jim Radford and David Caldwell wrote a neat little utility that lets you check
in select portions of a file into Darcs, Git, CVS, Subversion, or Mercurial. It
comes as a command line app and also and emacs interface.

A blog entry (http://porkrind.org/missives/commit-patch-managing-your-mess)
about commit-patch provides some detailed information on why you might want to
use commit-patch.

%prep
%setup -q

%install
rm -Rf %{buildroot}
install -d %{buildroot}/%{_bindir} %{buildroot}/%{_mandir}/man1/ %{buildroot}/%{_datadir}/emacs/site-lisp
install -m 755 %{name} %{buildroot}/%{_bindir}
install -m 644 %{name}.1 %{buildroot}/%{_mandir}/man1/
install -m 644 *.el %{buildroot}/%{_datadir}/emacs/site-lisp/
ln -s %{name} %{buildroot}/%{_bindir}/commit-partial
ln -s %{name}.1.%{_extension} %{buildroot}/%{_mandir}/man1/%{name}.1.%{_extension}

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/commit-*
%{_mandir}/man1/commit-*.*
%{_datadir}/emacs/site-lisp/%{name}*.el
