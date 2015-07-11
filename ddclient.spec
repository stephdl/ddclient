Summary: A client to update host entries on DynDNS like services
Name: ddclient
Version: 3.8.3
Release: 9%{?dist}
License: GPL
Group: System Environment/Base
URL: http://ddclient.sourceforge.net/
Source0: http://downloads.sourceforge.net/ddclient/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: perl(IO::Socket::SSL)
#Patch0: ddclient-3.8.3.IO::Socket.patch
%description
DDclient is a small full featured client requiring only Perl and no
additional modules. It runs under most UNIX OSes and has been tested
under Linux and FreeBSD. Supported features include: operating as a
daemon, manual and automatic updates, static and dynamic updates,
optimized updates for multiple addresses, MX, wildcards, abuse
avoidance, retrying failed updates, and sending update status to
syslog and through e-mail. This release may now obtain your IP address
from any interface, web based IP detection, Watchguard's SOHO router,
Netopia's R910 router, SMC's Barricade broadband router, Netgear's
RT3xx router, Linksys' broadband routers, MaxGate's UGATE-3x00
routers, ELSA's LANCOM DSL/10 routers, Cisco's 2610, 3com 3c886a 56k
Lan Modem, SOHOWare BroadGuard NBG800, almost every other router with
user configurable FW definitions (see the sample-etc_ddclient.conf)
and now provides Full support for DynDNS.org's NIC2 protocol. Support
is also included for other dynamic DNS services. Comes with sample
scripts for use with DHCP, PPP, and cron. See the README for more
information.

%prep
%setup -q
#%patch0 -p1
%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}{%{_sbindir},%{_sysconfdir}/ddclient,%{_initrddir}}
install -p ddclient %{buildroot}%{_sbindir}
install -p -m 0600 sample-etc_ddclient.conf %{buildroot}%{_sysconfdir}/ddclient/ddclient.conf
touch %{buildroot}%{_sysconfdir}/ddclient.cache
install -p sample-etc_rc.d_init.d_ddclient.redhat %{buildroot}%{_initrddir}/ddclient
chmod -x sample*
mkdir -p %{buildroot}%{_localstatedir}/cache/ddclient

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add ddclient

%preun
if [ $1 = 0 ]; then
        /sbin/service ddclient stop > /dev/null 2>&1
        /sbin/chkconfig --del ddclient
fi

%files
%defattr(-,root,root,-)
%doc sample* README* COPYRIGHT COPYING
%{_sbindir}/ddclient
%dir %{_sysconfdir}/ddclient
%config(noreplace) %{_sysconfdir}/ddclient/ddclient.conf
%config(noreplace) %ghost %{_sysconfdir}/ddclient.cache
%{_initrddir}/ddclient
%{_localstatedir}/cache/ddclient

%changelog
* Mon Jan 16 2012 Axel Thimm <Axel.Thimm@ATrpms.net> - 3.8.1-9
- Update to 3.8.1.

* Sun Mar  1 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 3.8.0-8
- Update to 3.8.0.

* Sun Aug 12 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 3.7.3-7
- Update to 3.7.3.
- Fix bug #1228 (Phil Anderson <pza@pza.net.au>)
- Fix bug #1238 (Martin Jürgens <mjuergens@gmail.com>)

* Thu May 24 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 3.7.1-6
- Update to 3.7.1.

* Wed Dec 28 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 3.6.7.

* Sun Jul  6 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.


