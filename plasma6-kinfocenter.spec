%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230520

Name: kinfocenter
Version: 5.240.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/kinfocenter/-/archive/master/kinfocenter-master.tar.bz2#/kinfocenter-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
%endif
Summary: KDE Plasma 6 Info Center
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6Wayland)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Plasma)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(libraw1394)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(libraw1394)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: systemsettings
BuildRequires: vulkan-tools
BuildRequires: wayland-utils
BuildRequires: xdpyinfo
BuildRequires: eglinfo
BuildRequires: glxinfo
BuildRequires: pciutils
BuildRequires: dmidecode
%ifarch %{x86_64} %{ix86} %{aarch64}
BuildRequires: fwupd
BuildRequires: aha
%endif
BuildRequires: clinfo
Requires: plasma6-systemsettings
Requires: vulkan-tools
Requires: wayland-utils
Requires: xdpyinfo
Requires: eglinfo
Requires: glxinfo
Requires: pciutils
Requires: dmidecode
%ifarch %{x86_64} %{ix86} %{aarch64}
Requires: fwupd
Requires: aha
%endif
Requires: clinfo
Obsoletes: about-distro

%description
KDE Plasma 6 Info Center.

%prep
%autosetup -p1 -n kinfocenter-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang kinfocenter --all-name --with-html

%files -f kinfocenter.lang
%{_sysconfdir}/xdg/menus/kinfocenter.menu
%{_bindir}/kinfocenter
%{_libdir}/libKInfoCenterInternal.so
%{_qtdir}/qml/org/kde/kinfocenter
%{_qtdir}/plugins/plasma/kcms/*.so
%{_qtdir}/plugins/plasma/kcms/kinfocenter/*.so
%{_datadir}/metainfo/org.kde.kinfocenter.appdata.xml
%{_datadir}/applications/org.kde.kinfocenter.desktop
%{_datadir}/desktop-directories/kinfocenter.directory
%{_datadir}/kinfocenter/categories/*.desktop
%{_libdir}/libexec/kauth/kinfocenter-dmidecode-helper
%{_datadir}/applications/kcm_about-distro.desktop
%{_datadir}/dbus-1/system-services/org.kde.kinfocenter.dmidecode.service
%{_datadir}/dbus-1/system.d/org.kde.kinfocenter.dmidecode.conf
%{_datadir}/polkit-1/actions/org.kde.kinfocenter.dmidecode.policy
%{_datadir}/applications/kcm_energyinfo.desktop
%{_datadir}/kinfocenter/firmware_security
