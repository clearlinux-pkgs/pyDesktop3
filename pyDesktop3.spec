#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyDesktop3
Version  : 0.5.2
Release  : 1
URL      : https://github.com/eight04/pyDesktop3/archive/v0.5.2.tar.gz
Source0  : https://github.com/eight04/pyDesktop3/archive/v0.5.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0
Requires: pyDesktop3-python = %{version}-%{release}
Requires: pyDesktop3-python3 = %{version}-%{release}
Requires: docutils
BuildRequires : buildreq-distutils3
BuildRequires : docutils

%description
desktop3
========
This is a python 3 port of `desktop <https://pypi.python.org/pypi/desktop>`__ package.

%package python
Summary: python components for the pyDesktop3 package.
Group: Default
Requires: pyDesktop3-python3 = %{version}-%{release}
Provides: pydesktop3-python

%description python
python components for the pyDesktop3 package.


%package python3
Summary: python3 components for the pyDesktop3 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyDesktop3 package.


%prep
%setup -q -n pyDesktop3-0.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565653850
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
