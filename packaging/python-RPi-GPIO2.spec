# python-RPi-GPIO2.spec
%global pypi_name	RPi.GPIO2
%global srcname		RPi-GPIO2

Summary: A libgpiod compatibility layer for the RPi.GPIO API
Name: python-%{srcname}
Version: 0.3.0
Release: 1%{?dist}
License: GPLv3+
URL: https://pypi.org/project/RPi.GPIO2/
Source0: https://github.com/underground-software/RPi.GPIO2/archive/v0.3.0a3.tar.gz

%global _description %{expand:
This library implements a compatibility layer between RPi.GPIO syntax and
libgpiod semantics, allowing a fedora user on the Raspberry Pi platform to
use the popular RPi.GPIO API, the original implmenetation of which depends
on features provided by a non-mainline kernel.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}


# This explicit dependency on the libgpiod python bindings subpackage
# is neccessary because it is unsatisfiable via PyPi
Requires: python3-libgpiod >= 1.5
BuildArch: noarch

# This package is pure python code so debuginfo is useless
%global debug_package %{nil}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{pypi_name}-%{version}a3

%build
%py3_build

%install
%py3_install

%check
rm -rf %{buildroot}%{python3_sitelib}/examples
rm -rf %{buildroot}%{python3_sitelib}/tests

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/RPi/
%{python3_sitelib}/%{pypi_name}-%{version}a3-py%{python3_version}.egg-info

%changelog
* Wed Aug 19 2020 Joel Savitz <joelsavitz@gmail.com> - 0.3.0-1
- initial package
