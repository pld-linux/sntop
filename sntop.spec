Summary:	A curses-based top-esque monitor of network host status
Summary(pl.UTF-8):	Bazowany na ncurses monitor stanu hostów w sieci (podobny do topa)
Name:		sntop
Version:	1.4.3
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/sntop/%{name}-%{version}.tar.gz
# Source0-md5:	0e99c64ea5a1bad6c1a32ac0dc2e9dd9
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-alarm_exec.patch
URL:		http://sntop.sourceforge.net/
BuildRequires:	ncurses-devel
Requires:	fping
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl.UTF-8
sntop jest bazowanym na ncurses podobnym do topa terminalowym
narzędziem do monitorowania łączności hostów w sieci, wspierający
różne dodatki.

sntop używa fpinga (ping też jest obsługiwany) do ustalenia łączności
między hostami wyszczególnionymi w pliku konfiguracyjnym co ustalony
czas. Rezultaty są wyświetlane w postaci podobnej do topa.

Rozszerzone możliwości to generowanie HTML z rezultatami na
automatyczną stronę WWW, tryb bezpiecznego terminala, wykonywanie
zewnętrznego programu podczas alarmu (host nie działający lub zmiana
stanu hosta), obsługa koloru, pliki konfiguracyjne dla systemu i
użytkownika.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}

%{__make} install \
	INSTDIR=$RPM_BUILD_ROOT%{_bindir} \
	ETCDIR=$RPM_BUILD_ROOT%{_sysconfdir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CREDITS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sntoprc
%attr(755,root,root) %{_bindir}/sntop
%{_mandir}/man1/sntop.1*
