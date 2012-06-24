#
# TODO:
#  - init script (see contrib/)
#
# generate new snap:
# 	git clone git://gitorious.org/kvmsh/kvmsh.git
#	cd kvmsh
#	D=$(date '+%Y%m%d'); git archive master --prefix kvmsh-$D/ | bzip2 -f9 > kvmsh-$D.tar.bz2
#
%define snap	20090905
%include	/usr/lib/rpm/macros.perl
Summary:	kernel-based Virtual Machines manager
Summary(pl.UTF-8):	Zarządca maszyn wirtualnych KVM
Name:		kvmsh
Version:	0
Release:	0.%{snap}.1
License:	GPL v2
Group:		Applications
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	0f731b1fcfb3661abe33326e6cfeed56
URL:		http://gitorious.org/kvmsh/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line interface to manage Kernel-based Virtual Machines (KVM)
on headless machines.

%description -l pl.UTF-8
Interfejs tekstowy do zarządzania maszynami wirtualnymi stworzonymi za
pomocą KVM.

%package -n bash-completion-kvmsh
Summary:	bash-completion for kvmsh
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla kvmsh
Group:		Applications/Shells
Requires:	bash-completion

%description -n bash-completion-kvmsh
This package provides bash-completion for kvmsh.

%description -n bash-completion-kvmsh -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla kvmsh.

%prep
%setup -q -n %{name}-%{snap}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{5,8}}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/

install src/kvmsh.pl $RPM_BUILD_ROOT%{_bindir}/kvmsh
install doc/man/kvmsh.8 $RPM_BUILD_ROOT%{_mandir}/man8
install doc/man/kvmdomain.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5
install contrib/bash_completion $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/kvmsh-completion.bash

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO doc/examples
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man5/kvmdomain.conf.5*
%{_mandir}/man8/kvmsh.8*

%files -n bash-completion-kvmsh
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/*
