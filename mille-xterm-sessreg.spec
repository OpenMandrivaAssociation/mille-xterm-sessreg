%define svn 2137

Summary:	X session register for the MILLE-XTERM project
Name:		mille-xterm-sessreg
Version:	1.0
Release:	%mkrel 0.%{svn}.3
License:	GPL
Group:		System/Servers
URL:		http://www.revolutionlinux.com/mille-xterm
Source:		mille-xterm-sessreg-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This program replaces sessreg by a statically linked version that does not
depend on any X libraries. It doesn't use lastlog, only utmp.

%prep

%setup -q

%build 

gcc %{optflags} -DNO_LASTLOG sessreg.c -o mille-xterm-sessreg

%install
rm -fr %{buildroot}

install -d  %{buildroot}%{_bindir}
install -m0755 mille-xterm-sessreg %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS Changelog COPYING INSTALL README add1000users del1000users
%{_bindir}/mille-xterm-sessreg




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.2137.3mdv2011.0
+ Revision: 620337
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-0.2137.2mdv2010.0
+ Revision: 430035
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-0.2137.1mdv2008.1
+ Revision: 136579
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.2137.1mdv2007.0
+ Revision: 117817
- Import mille-xterm-sessreg

* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.2137.1mdk
- initial Mandriva package (mille-xterm import)

