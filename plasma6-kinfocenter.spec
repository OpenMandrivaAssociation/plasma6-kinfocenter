%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: plasma6-kinfocenter
Version: 6.3.2
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/kinfocenter/-/archive/%{gitbranch}/kinfocenter-%{gitbranchd}.tar.bz2#/kinfocenter-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/kinfocenter-%{version}.tar.xz
%endif
Summary: KDE Plasma 6 Info Center
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Wayland) >= 5.90.0
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
BuildRequires: cmake(Plasma) >= 5.90.0
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6Auth)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(libdrm)
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
Requires: vulkan-tools
Requires: (wayland-utils if kf6-kwindowsystem-backend-wayland)
Requires: (xdpyinfo if kf6-kwindowsystem-backend-x11)
Requires: eglinfo
Requires: glxinfo
Requires: pciutils
Requires: dmidecode
%ifarch %{x86_64} %{ix86} %{aarch64}
Requires: fwupd
Requires: aha
%endif
Requires: clinfo
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DBUILD_WITH_QT6:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE Plasma 6 Info Center.

%install -a
%find_lang kinfocenter --all-name --with-html

%files -f kinfocenter.lang
%{_bindir}/kinfocenter
%{_libdir}/libKInfoCenterInternal.so
%{_qtdir}/qml/org/kde/kinfocenter
%{_qtdir}/plugins/plasma/kcms/*.so
%{_qtdir}/plugins/plasma/kcms/kinfocenter/*.so
%{_datadir}/metainfo/org.kde.kinfocenter.appdata.xml
%{_datadir}/applications/org.kde.kinfocenter.desktop
%{_libdir}/libexec/kinfocenter-opengl-helper
%{_libdir}/libexec/kf6/kauth/kinfocenter-dmidecode-helper
%{_datadir}/applications/kcm_about-distro.desktop
%{_datadir}/dbus-1/system-services/org.kde.kinfocenter.dmidecode.service
%{_datadir}/dbus-1/system.d/org.kde.kinfocenter.dmidecode.conf
%{_datadir}/polkit-1/actions/org.kde.kinfocenter.dmidecode.policy
%{_datadir}/applications/kcm_energyinfo.desktop
%{_datadir}/kinfocenter
