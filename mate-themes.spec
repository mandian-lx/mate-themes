%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Themes for MATE
Name:		mate-themes
Version:	1.8.1
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:	icon-naming-utils
BuildRequires:	mate-common
BuildRequires:	pkgconfig(gtk-engines-2)
Requires:	gtk-engines2
Requires:	mate-icon-theme
Requires:	murrine

%description
This packages contains Themes for MATE.

%prep
%setup -q

%build
%configure \
	--build=%{_host}

%make

%install
%makeinstall_std

%find_lang %{name}

for t in ContrastHigh-SVG ContrastHighLargePrint ContrastHighLargePrintInverse Fog Quid; do
	touch %{buildroot}%{_iconsdir}/$t/icon-theme.cache
done

%post
for t in ContrastHigh-SVG ContrastHighLargePrint ContrastHighLargePrintInverse Fog Quid; do
	touch --no-create %{_iconsdir}/$t &>/dev/null || :
done

%posttrans
for t in ContrastHigh-SVG ContrastHighLargePrint ContrastHighLargePrintInverse Fog Quid; do
	gtk-update-icon-cache %{_iconsdir}/$t &>/dev/null || :
done

%postun
if [ $1 -eq 0 ] ; then
	for t in ContrastHigh-SVG ContrastHighLargePrint ContrastHighLargePrintInverse Fog Quid; do
		touch --no-create %{_iconsdir}/$t &>/dev/null || :
		gtk-update-icon-cache %{_iconsdir}/$t &>/dev/null || :
	done
fi

%files -f %{name}.lang
%doc README NEWS AUTHORS 
%{_iconsdir}/ContrastHigh-SVG/*
%{_iconsdir}/ContrastHigh/index.theme
%{_iconsdir}/ContrastHighInverse/index.theme
%{_iconsdir}/ContrastHighLargePrint/*
%{_iconsdir}/ContrastHighLargePrintInverse/*
%{_iconsdir}/Fog/*
%{_iconsdir}/MateLargePrint/index.theme
%{_iconsdir}/Quid/*
%{_iconsdir}/mate/cursors/*
%{_datadir}/themes/AlaDelta/*
%{_datadir}/themes/Atantla/metacity-1/metacity-theme-1.xml

%doc %{_datadir}/themes/BlackMATE/README
%doc %{_datadir}/themes/BlueMenta/COPYING
%doc %{_datadir}/themes/BlueMenta/README
%doc %{_datadir}/themes/GreenLaguna/README
%doc %{_datadir}/themes/Menta/COPYING
%doc %{_datadir}/themes/Menta/README

%{_datadir}/themes/BlackMATE/cinnamon
%{_datadir}/themes/BlackMATE/gtk-2.0
%{_datadir}/themes/BlackMATE/gtk-3.0
%{_datadir}/themes/BlackMATE/index.theme
%{_datadir}/themes/BlackMATE/metacity-1

%{_datadir}/themes/BlackMenta/metacity-1

%{_datadir}/themes/BlueMenta/cinnamon
%{_datadir}/themes/BlueMenta/gtk-2.0
%{_datadir}/themes/BlueMenta/gtk-3.0
%{_datadir}/themes/BlueMenta/index.theme
%{_datadir}/themes/BlueMenta/metacity-1
%{_datadir}/themes/BlueMenta/unity
%{_datadir}/themes/BlueMenta/xfwm4

%{_datadir}/themes/ContrastHigh/gtk-3.0
%{_datadir}/themes/ContrastHigh/metacity-1
%{_datadir}/themes/ContrastHigh/gtk-2.0/*
%{_datadir}/themes/ContrastHigh/index.theme
%{_datadir}/themes/ContrastHighInverse/gtk-2.0/*
%{_datadir}/themes/ContrastHighInverse/index.theme
%{_datadir}/themes/ContrastHighLargePrint/gtk-2.0/gtkrc
%{_datadir}/themes/ContrastHighLargePrint/index.theme.disabled
%{_datadir}/themes/ContrastHighLargePrint/pixmaps/*
%{_datadir}/themes/ContrastHighLargePrintInverse/gtk-2.0/gtkrc
%{_datadir}/themes/ContrastHighLargePrintInverse/index.theme.disabled
%{_datadir}/themes/ContrastHighLargePrintInverse/pixmaps/*

%{_datadir}/themes/ContrastLow/gtk-2.0/gtkrc
%{_datadir}/themes/ContrastLow/index.theme.disabled
%{_datadir}/themes/ContrastLowLargePrint/gtk-2.0/gtkrc
%{_datadir}/themes/ContrastLowLargePrint/index.theme.disabled
%{_datadir}/themes/ContrastLowLargePrint/pixmaps/*

%{_datadir}/themes/GreenLaguna/gtk-3.0
%{_datadir}/themes/GreenLaguna/gtk-2.0
%{_datadir}/themes/GreenLaguna/metacity-1
%{_datadir}/themes/GreenLaguna/index.theme

%{_datadir}/themes/Menta/cinnamon
%{_datadir}/themes/Menta/gtk-2.0
%{_datadir}/themes/Menta/gtk-3.0
%{_datadir}/themes/Menta/index.theme
%{_datadir}/themes/Menta/metacity-1
%{_datadir}/themes/Menta/unity
%{_datadir}/themes/Menta/xfwm4

%{_datadir}/themes/Fog/index.theme
%{_datadir}/themes/Fog/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/PrintLarge/gtk-2.0/gtkrc
%{_datadir}/themes/PrintLarge/index.theme.disabled

%{_datadir}/themes/Quid/index.theme
%{_datadir}/themes/Quid/metacity-1

%{_datadir}/themes/Reverse/gtk-2.0/gtkrc
%{_datadir}/themes/Reverse/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/Shiny/gtk-2.0/gtkrc
%{_datadir}/themes/Shiny/index.theme
%{_datadir}/themes/Shiny/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/Simply/gtk-2.0/gtkrc

%{_datadir}/themes/TraditionalGreen/gtk-2.0
%{_datadir}/themes/TraditionalGreen/gtk-3.0
%{_datadir}/themes/TraditionalGreen/index.theme
%{_datadir}/themes/TraditionalGreen/metacity-1

%{_datadir}/themes/TraditionalOk/index.theme
%{_datadir}/themes/TraditionalOk/metacity-1/metacity-theme-1.xml
%doc %{_datadir}/themes/TraditionalOk/doc
%{_datadir}/themes/TraditionalOk/gtk-2.0
%{_datadir}/themes/TraditionalOk/gtk-3.0
%{_datadir}/themes/TraditionalOk/openbox-3
%{_datadir}/themes/TraditionalOk/wallpapers
%{_datadir}/themes/TraditionalOk/xfwm4

