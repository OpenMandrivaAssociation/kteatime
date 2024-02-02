Summary:	System tray applet that makes sure your tea doesn't get too strong
Name:		plasma6-kteatime
Version:	24.01.95
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kteatime-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Widgets)

%description
System tray applet that makes sure your tea doesn't get too strong.

%files -f kteatime.lang
%{_bindir}/kteatime
%{_datadir}/applications/org.kde.kteatime.desktop
%{_iconsdir}/hicolor/*/apps/kteatime.*
%{_datadir}/metainfo/*.xml
%{_datadir}/knotifications6/*.notifyrc

#-------------------------------------------------------------------

%prep
%autosetup -p1 -n kteatime-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kteatime --with-html
