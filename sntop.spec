Summary:	A curses-based top-esque monitor of network host status
Summary(pl):	Bazowany na ncurses monitor stanu hostów w sieci (podobny do topa)
Name:		sntop
Version:	1.4.2
Release:	2
License:	GPL
Group:		Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		sntop-ncurses.patch
URL:		http://sntop.sourceforge.net/
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	fping

%description
sntop is an ncurses-based top-esque console utility for monitoring the
connectivity of network hosts, supporting various advanced features
and released under the GPL.

sntop uses fping (ping is supported, too) to determine connectivity of
hosts, specified in a config file, on a regular interval. the results
are displayed in a top-like format.

advanced features include html generation of results for automatic web
page, secure terminal mode, execution of external file on alarm
(configurable for either host DOWN or any change in host status),
color support, and both user and system-wide config files.

%description -l pl
sntop jest bazowanym na ncurses podobnym do topa terminalowym
narzêdziem do monitorowania ³±czno¶ci hostów w sieci, wspieraj±cy
ró¿ne dodatki.

sntop u¿ywa fpinga (ping te¿ jest obs³ugiwany) do ustalenia ³±czno¶ci
miêdzy hostami wyszczególnionymi w pliku konfiguracyjnym co ustalony
czas. Rezultaty s± wy¶wietlane w postaci podobnej do topa.

Rozszerzone mo¿liwo¶ci to generowanie HTML z rezultatami na
automatyczn± stronê WWW, tryb bezpiecznego terminala, wykonywanie
zewnêtrznego programu podczas alarmu (host nie dzia³aj±cy lub zmiana
stanu hosta), obs³uga koloru, pliki konfigurcyjne dla systemu i
u¿ytkownika.

%prep
%setup -q

%patch0 -p1

%build
%configure2_13 


%{__make}   

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}
%{__make} install INSTDIR=$RPM_BUILD_ROOT%{_bindir} ETCDIR=$RPM_BUILD_ROOT%{_sysconfdir} MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1


gzip -9nf ChangeLog CREDITS  TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_sysconfdir}/sntoprc
%attr(755,root,root) %{_bindir}/sntop
%{_mandir}/man1/sntop.1.gz
