%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Themes for MATE
Name:		mate-themes
Version:	3.22.12
Release:	1
License:	LGPLv2+ and GPLv2+ and GPLv3+
Group:		Graphical desktop/GNOME
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/themes/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	icon-naming-utils
BuildRequires:	mate-common
BuildRequires:	pkgconfig(gtk-engines-2)

Requires:	gtk-engines2
Requires:	mate-icon-theme
Requires:	murrine

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This packages provides Themes for MATE.

%files
%doc README NEWS AUTHORS
%{_iconsdir}/mate/cursors/*
# BlackMATE
%dir %{_datadir}/themes/BlackMATE/
%{_datadir}/themes/BlackMATE/apps
%{_datadir}/themes/BlackMATE/cinnamon
%{_datadir}/themes/BlackMATE/gtk-2.0
%{_datadir}/themes/BlackMATE/gtk-3.0
%{_datadir}/themes/BlackMATE/index.theme
%{_datadir}/themes/BlackMATE/metacity-1
%{_datadir}/themes/BlackMATE/unity
%doc %{_datadir}/themes/BlackMATE/README
%doc %{_datadir}/themes/BlackMATE/COPYING
# BlueMenta
%dir %{_datadir}/themes/BlueMenta/
%{_datadir}/themes/BlueMenta/cinnamon
%{_datadir}/themes/BlueMenta/emerald
%{_datadir}/themes/BlueMenta/gtk-2.0
%{_datadir}/themes/BlueMenta/gtk-3.0
%{_datadir}/themes/BlueMenta/index.theme
%{_datadir}/themes/BlueMenta/metacity-1
%{_datadir}/themes/BlueMenta/unity
%{_datadir}/themes/BlueMenta/xfwm4
%doc %{_datadir}/themes/BlueMenta/README
%doc %{_datadir}/themes/BlueMenta/COPYING
# Blue-Submarine
%dir %{_datadir}/themes/Blue-Submarine/
%{_datadir}/themes/Blue-Submarine/cinnamon
%{_datadir}/themes/Blue-Submarine/emerald
%{_datadir}/themes/Blue-Submarine/gtk-2.0
%{_datadir}/themes/Blue-Submarine/gtk-3.0
%{_datadir}/themes/Blue-Submarine/index.theme
%{_datadir}/themes/Blue-Submarine/metacity-1
# ContrastHighInverse
%dir %{_datadir}/themes/ContrastHighInverse/
%{_datadir}/themes/ContrastHighInverse/gtk-2.0
%{_datadir}/themes/ContrastHighInverse/gtk-3.0
%{_datadir}/themes/ContrastHighInverse/index.theme
%{_datadir}/themes/ContrastHighInverse/metacity-1
%{_datadir}/themes/ContrastHighInverse/pixmaps
# GreenLaguna
%dir %{_datadir}/themes/GreenLaguna/
%{_datadir}/themes/GreenLaguna/gtk-3.0
%{_datadir}/themes/GreenLaguna/gtk-2.0
%{_datadir}/themes/GreenLaguna/metacity-1
%{_datadir}/themes/GreenLaguna/index.theme
%{_datadir}/themes/GreenLaguna/unity
%doc %{_datadir}/themes/GreenLaguna/README
%doc %{_datadir}/themes/GreenLaguna/COPYING
# Green-Submarine
%dir %{_datadir}/themes/Green-Submarine/
%{_datadir}/themes/Green-Submarine/cinnamon
%{_datadir}/themes/Green-Submarine/emerald
%{_datadir}/themes/Green-Submarine/gtk-3.0
%{_datadir}/themes/Green-Submarine/gtk-2.0
%{_datadir}/themes/Green-Submarine/metacity-1
%{_datadir}/themes/Green-Submarine/index.theme
# HighContrast
%dir %{_datadir}/themes/HighContrast/
%{_datadir}/themes/HighContrast/metacity-1
%dir %{_iconsdir}/ContrastHigh/
%{_iconsdir}/ContrastHigh/16x16
%{_iconsdir}/ContrastHigh/22x22
%{_iconsdir}/ContrastHigh/24x24
%{_iconsdir}/ContrastHigh/32x32
%{_iconsdir}/ContrastHigh/48x48
%{_iconsdir}/ContrastHigh/256x256
%{_iconsdir}/ContrastHigh/icon-theme.cache
%{_iconsdir}/ContrastHigh/index.theme
%{_iconsdir}/ContrastHigh/scalable
# Menta
%dir %{_datadir}/themes/Menta/
%{_datadir}/themes/Menta/cinnamon
%{_datadir}/themes/Menta/emerald
%{_datadir}/themes/Menta/gtk-2.0
%{_datadir}/themes/Menta/gtk-3.0
%{_datadir}/themes/Menta/index.theme
%{_datadir}/themes/Menta/metacity-1
%{_datadir}/themes/Menta/unity
%{_datadir}/themes/Menta/xfwm4
%doc %{_datadir}/themes/Menta/README
%doc %{_datadir}/themes/Menta/COPYING
# Shiny
%dir %{_datadir}/themes/Shiny/
%{_datadir}/themes/Shiny/metacity-1
# TraditionalGreen
%dir %{_datadir}/themes/TraditionalGreen/
%{_datadir}/themes/TraditionalGreen/gtk-2.0
%{_datadir}/themes/TraditionalGreen/gtk-3.0
%{_datadir}/themes/TraditionalGreen/index.theme
%{_datadir}/themes/TraditionalGreen/metacity-1
%doc %{_datadir}/themes/TraditionalGreen/COPYING
# TraditionalOk
%dir %{_datadir}/themes/TraditionalOk/
%{_datadir}/themes/TraditionalOk/gtk-2.0
%{_datadir}/themes/TraditionalOk/gtk-3.0
%{_datadir}/themes/TraditionalOk/index.theme
%{_datadir}/themes/TraditionalOk/metacity-1
%{_datadir}/themes/TraditionalOk/openbox-3
%{_datadir}/themes/TraditionalOk/xfwm4
%doc %{_datadir}/themes/TraditionalOk/COPYING

#---------------------------------------------------------------------------

%prep
%setup -q

%build
#NOCONFIGURE=yes ./autogen.sh
%configure
%make

%install
%makeinstall_std

for t in ContrastHigh; do
	touch %{buildroot}%{_iconsdir}/$t/icon-theme.cache
done

%post
for t in ContrastHigh; do
	touch --no-create %{_iconsdir}/$t &>/dev/null || :
done

%posttrans
for t in ContrastHigh; do
	gtk-update-icon-cache %{_iconsdir}/$t &>/dev/null || :
done

%postun
if [ $1 -eq 0 ] ; then
	for t in ContrastHigh; do
		touch --no-create %{_iconsdir}/$t &>/dev/null || :
		gtk-update-icon-cache %{_iconsdir}/$t &>/dev/null || :
	done
fi

