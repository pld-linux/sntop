#
# scamlib RPM Spec File - 06 May 2001
#

Summary:	a curses-based top-esque monitor of network host status
Name:		sntop
Version:	1.4.2
Release:	1
License:	GPL
Group:		Applications
Source0:	http://sntop.sourceforge.net/files/%{name}-%{version}.tar.gz
URL:		http://sntop.sourceforge.net/
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

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir} --bindir=%{_bindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
rm -rf %{buildroot}
%{__make} install

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING CREDITS README TODO
%{_sysconfdir}/sntoprc
%attr(755,root,root) %{_bindir}/sntop
%{_mandir}/man1/sntop.1.gz
