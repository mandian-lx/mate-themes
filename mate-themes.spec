Summary:	Themes for MATE
Name:		mate-themes
Version:	1.2.2
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz
BuildArch: noarch

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
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--build=%_host

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
%{_datadir}/themes/Aldabra/gtk-2.0/*
%{_datadir}/themes/Aldabra/gtk-3.0/*
%{_datadir}/themes/Aldabra/index.theme
%{_datadir}/themes/Aldabra/metacity-1/*
%{_datadir}/themes/Atantla/metacity-1/metacity-theme-1.xml
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
%{_datadir}/themes/Fog/index.theme
%{_datadir}/themes/Fog/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/PrintLarge/gtk-2.0/gtkrc
%{_datadir}/themes/PrintLarge/index.theme.disabled
%{_datadir}/themes/Quid/index.theme
%{_datadir}/themes/Reverse/gtk-2.0/gtkrc
%{_datadir}/themes/Reverse/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/Shiny/gtk-2.0/gtkrc
%{_datadir}/themes/Shiny/index.theme
%{_datadir}/themes/Shiny/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/Simply/gtk-2.0/gtkrc
%{_datadir}/themes/TraditionalOk/index.theme
%{_datadir}/themes/TraditionalOk/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/TraditionalOkClassic/gtk-2.0/gtkrc
%{_datadir}/themes/TraditionalOkClassic/metacity-1/metacity-theme-1.xml

