Name:           python-pywlroots
Version:        0.17.0
Release:        1
Summary:        Python binding to the wlroots library using cffi
License:        NCSA

URL:            https://github.com/flacjacket/pywlroots
Source0:        https://files.pythonhosted.org/packages/source/p/pywlroots/pywlroots-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: (pkgconfig(wlroots) >= 0.17.0 with pkgconfig(wlroots) < 0.18)
BuildSystem:  python


%description
A Python binding to the wlroots library using cffi. The library uses pywayland
to provide the Wayland bindings and python-xkbcommon to provide wlroots
keyboard functionality.}


%files
%license LICENSE
%doc README.rst
%{python_sitelib}/pywlroots-%{version}.dist-info
%{python_sitelib}/pywlroots/
