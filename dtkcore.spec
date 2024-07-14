Name:           dtkcore
Version:        5.6.32
Release:        1
Summary:        Deepin tool kit core modules
License:        LGPLv3+
Group:          System/Deepin
URL:            https://github.com/linuxdeepin/dtkcore
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  doxygen
BuildRequires:  cmake(Dtk)
#BuildRequires:  annobin
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  gtest-devel
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(icu-uc)

%description
Deepin tool kit core modules.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcommon-devel
Requires:       qt5-qtbase-devel%{?_isa}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.5*
%dir %{_libexecdir}/dtk5/
%{_libexecdir}/dtk5/dtk-settings
%{_libexecdir}/dtk5/dtk-license.py
%{_libexecdir}/dtk5/dtk-translate.py
%{_libexecdir}/dtk5/deepin-os-release
%{_prefix}/bin/qdbusxml2cpp-fix

%files devel
%doc doc/Specification.md
%{_includedir}/libdtk-*/
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_libdir}/cmake/DtkCore/
%{_libdir}/cmake/DtkCMake/
%{_libdir}/cmake/DtkTools/
%{_libdir}/pkgconfig/dtkcore.pc
%{_libdir}/lib%{name}.so
