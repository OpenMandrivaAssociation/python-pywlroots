%undefine _debugsource_packages
Name:           python-pywlroots
Version:        0.17.0
Release:        3
Summary:        Python binding to the wlroots library using cffi
License:        NCSA
Group:          Development/Python

URL:            https://github.com/flacjacket/pywlroots
Source0:        https://files.pythonhosted.org/packages/source/p/pywlroots/pywlroots-%{version}.tar.gz

BuildRequires: pkgconfig(python3)
# pywlroots 0.17 binds wlroots 0.17. pkgconfig(wlroots) is also provided by
# the 0.16 and 0.19 devel packages, so depend on the versioned package.
BuildRequires: %mklibname wlroots0.17 -d
BuildRequires: python%{pyver}dist(pywayland)
BuildRequires: python%{pyver}dist(setuptools)
BuildRequires: python%{pyver}dist(pip)
BuildRequires: python%{pyver}dist(wheel)
BuildRequires: python%{pyver}dist(xkbcommon)
BuildRequires: python%{pyver}dist(cffi)
Requires:  python-xkbcommon
Requires:  python%{pyver}dist(pywayland)
Requires:  python%{pyver}dist(cffi)

%description
A Python binding to the wlroots library using cffi. The library uses pywayland
to provide the Wayland bindings and python-xkbcommon to provide wlroots
keyboard functionality.

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
%{python_sitearch}/pywlroots-%{version}.dist-info
%{python_sitearch}/wlroots/
