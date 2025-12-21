%undefine _debugsource_packages
Name:           python-pywlroots
Version:        0.17.0
Release:        2
Summary:        Python binding to the wlroots library using cffi
License:        NCSA

URL:            https://github.com/flacjacket/pywlroots
Source0:        https://files.pythonhosted.org/packages/source/p/pywlroots/pywlroots-%{version}.tar.gz

BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(wlroots-0.19)
BuildRequires: python%{pyver}dist(pywayland)
BuildRequires: python%{pyver}dist(setuptools)
BuildRequires: python%{pyver}dist(pip)
BuildRequires: python%{pyver}dist(xkbcommon)
BuildRequires: python%{pyver}dist(cffi)
Requires:  python-xkbcommon
Requires:  python%{pyver}dist(pywayland)

%description
A Python binding to the wlroots library using cffi. The library uses pywayland
to provide the Wayland bindings and python-xkbcommon to provide wlroots
keyboard functionality.}

%prep
%autosetup -n pywlroots-%{version} -p1

%build
python ./wlroots/ffi_build.py
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/pywlroots-%{version}.dist-info
%{python_sitelib}/wlroots/
