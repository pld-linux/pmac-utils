Summary:	PowerPC Linux system utilities
Summary(pl):	Narzêdzia systemowe dla PowerPC
Name:		pmac-utils
Version:	2.1
Release:	5
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-2.1-ydl.patch
BuildRequires:	sgml-tools
ExclusiveArch:	ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PowerPC Linux specific applications including macos (a script to
reboot to the mac OS), nvsetenv (a tool to manipulate Open Firmware
variables), and nvvideo (a tool to manipulate the video settings
stored in PRAM).

%description -l pl
Aplikacje specyficzne dla architektury PowerPC takie jak:
- macos - skrypt do restartu systemu MacOS,
- nvsetenv - narzêdzie do konfiguracji zmiennych Open Firmware,
- nvvideo - narzêdzie do konfiguracji parametrów obrazu w PRAM.

%prep
%setup -q -n pmac-utils-%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT exec_prefix=%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/macos
%attr(755,root,root) %{_sbindir}/nvsetenv
%attr(755,root,root) %{_sbindir}/nvvideo
%{_mandir}/man8/*
