%define svn 2137

Summary:	X session register for the MILLE-XTERM project
Name:		mille-xterm-sessreg
Version:	1.0
Release:	%mkrel 0.%{svn}.1
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


