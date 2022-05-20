%global srcname d2to1

Name: python-%{srcname}
Version: 0.2.12.post1
Release: 1
Summary: Allows using distutils2-like setup.cfg files with setup.py
License: BSD

URL: http://pypi.python.org/pypi/d2to1
Source0: https://pypi.python.org/packages/source/d/d2to1/d2to1-0.2.12.post1.tar.gz

BuildArch: noarch

%global _description\
d2to1 allows using distutils2-like setup.cfg files for a package's metadata\
with a distribute/setuptools setup.py script. It works by providing a\
distutils2-formatted setup.cfg file containing all of a package's metadata,\
and a very minimal setup.py which will slurp its arguments from the setup.cfg.

%description %_description

%package -n python3-d2to1
Summary: Allows using distutils2-like setup.cfg files with setup.py
%{?python_provide:%python_provide python3-d2to1}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:  python3-setuptools

%description -n python3-d2to1 %_description

%prep
%setup -q -n %{srcname}-%{version}

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%py3_build

%install
%py3_install

%files -n python3-d2to1
%doc CHANGES.rst README.rst
%license LICENSE
%{python3_sitelib}/*


%changelog
* Tue May 17 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 0.2.12.post1-1
- Initial package

