#
# scamlib RPM Spec File - 06 May 2001
#

Summary: a curses-based top-esque monitor of network host status
Name: sntop
Version: 1.4.2
Release: 1
Copyright: GPL
Group: System Environment/Daemons
Source: http://sntop.sourceforge.net/files/%{name}-%{version}.tar.gz
URL: http://sntop.sourceforge.net/
Requires: fping

%description
sntop is an ncurses-based top-esque console utility for monitoring the
connectivity of network hosts, supporting various advanced features and
released under the GPL.

sntop uses fping (ping is supported, too) to determine connectivity of hosts,
specified in a config file, on a regular interval. the results are displayed
in a top-like format.

advanced features include html generation of results for automatic web page,
secure terminal mode, execution of external file on alarm (configurable for
either host DOWN or any change in host status), color support, and both user
and system-wide config files.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir} --bindir=%{_bindir}
make

%install
rm -rf %{buildroot}
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc ChangeLog COPYING CREDITS README TODO
/etc/sntoprc
%{_bindir}/sntop
%{_mandir}/man1/sntop.1.gz

%changelog
* Thu May 17 2001 Robert M. Love <rml@tech9.net>
- initial packaging of 1.4.2
