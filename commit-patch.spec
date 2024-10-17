Name:		commit-patch
Version:	2.6
Release:	1
Summary:	A utility that lets you check select portions of a file into a VCS
License:	GPLv2
URL:		https://porkrind.org/commit-patch/
Group:		Text tools
Source:		http://porkrind.org/commit-patch/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch

%description
Jim Radford and David Caldwell wrote a neat little utility that lets you check
in select portions of a file into Darcs, Git, CVS, Subversion, or Mercurial. It
comes as a command line app and also and emacs interface.

A blog entry (http://porkrind.org/missives/commit-patch-managing-your-mess)
about commit-patch provides some detailed information on why you might want to
use commit-patch.

commit-patch and commit-partial can make commiting partial changes easier with:
-darcs
-git
-mercurial
-cvs
-svn

commit-patch-buffer.el is an emacs interface to commit-patch. It allows you to
just hit C-c C-c in any patch buffer to apply and commit only the changes
indicated by the patch, regardless of the changes in your working directory. 

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


%changelog
* Sat Nov 27 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.4-1mdv2011.0
+ Revision: 601820
- update to 2.4

* Fri Mar 26 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.3-1mdv2010.1
+ Revision: 527820
- update to 2.3

* Tue Oct 27 2009 Buchan Milne <bgmilne@mandriva.org> 2.2-1mdv2010.0
+ Revision: 459550
- import commit-patch


