Name: %{__username}-repo
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: package for user devel rhel9 redBorder repository	

Group: System Environment/Base
License: GPLv2
URL: https://github.com/dvanhoucke/redborder-repo
Source0: %{name}-%{version}.tar.gz
Requires: epel-release

%description
This package contains user devel rhel9 packages for redborder repository as well as configuration for yum.

%prep
%setup -qn %{name}-%{version}

%build
packaging/rpm/placeholders.sh -u %{__username} -v %{__version} -b %{__release}

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
install -D -m 644 resources/username.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/%{__username}.repo
install -D -m 644 resources/RPM-GPG-KEY-redborder-repo $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root)
/etc/yum.repos.d/%{__username}.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-redborder-repo

%changelog
* Thu Oct 26 2023 David Vanhoucke <dvanhoucke@redborder.com> - 0.0.2-1
- update rhel9
* Thu Jan 28 2020 David Vanhoucke <dvanhoucke@redborder.com> - 0.0.1-1
- first spec version
