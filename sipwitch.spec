%define major 1
%define libname %mklibname sipwitch %major
%define devname %mklibname sipwitch -d

Summary:	Secure peer-to-peer VoIP server
Name:		sipwitch
Version:	1.4.0
Release:	2
License:	GPLv3+
Group:		Networking/Instant messaging
URL:		https://www.gnu.org/software/sipwitch/
Source0:	http://ftp.gnu.org/gnu/sipwitch/%{name}-%{version}.tar.gz
Source1:	http://ftp.gnu.org/gnu/sipwitch/%{name}-%{version}.tar.gz.sig
Patch0:		sipwitch-1.4.0-mdv-configure.patch

BuildRequires:	exosip-devel
BuildRequires:	pkgconfig(ucommon)

%description
GNU SIP Witch is a secure peer-to-peer VoIP server that uses the SIP protocol.
Calls can be made peer-to-peer behind NAT firewalls, and without needing
a service provider. GNU SIP Witch does not perform codec operations and thereby
enables SIP endpoints to directly peer negotiate call setting and process peer
to peer media streaming even when when multiple SIP Witch call nodes
at multiple locations are involved. This means GNU SIP Witch operates
without introducing additional media latency or offering a central point
for media intercept or capture. GNU SIP Witch can be used to build secure
and intercept-free telephone systems that can operate over the public Internet.

GNU SIP Witch is designed to support network scaling of telephony services,
rather than the heavily compute-bound solutions we find in use today.
This means a call node has a local authentication/registration database,
and this will be mirrored, so that any active call node in a cluster will be
able to accept and service a call. This allows for the possibility of live
failover support in the future as well.

GNU SIP Witch is not a SIP "router", and does not try to address the same
things as a project like iptel "Ser". GNU SIP Witch is being designed to create
on-premise SIP telephone systems, telecenter servers, and Internet hosted SIP
telephone systems. One important feature will include use of URI routing
to support direct peer to peer calls between service domains over the public
Internet without needing mediation of an intermediary "service provider"
so that people can publish and call sip: uri's unconstrained. GNU SIP Witch is
about freedom to communicate and the removal of artificial barriers
and constraints whether imposed by monopoly service providers
or by governments.

%package -n %{libname}
Summary:	GNU SIP Witch shared library
Group:		System/Libraries

%description -n %{libname}
This package containg shared libraries for GNU SIP Witch.

%package -n %{devname}
Summary:	GNU SIP Witch development files
Group:		System/Libraries

%description -n %{devname}
This package containg development files for GNU SIP Witch library.

%prep
%setup -q
%autopatch -p1
autoreconf

%build
%configure2_5x \
	--disable-static \
	--enable-openssl \
	--with-initrddir=%{_initddir} \
	--with-cgibindir=%{_libdir}/%{name}/cgi-bin

%make

%install
%makeinstall_std

%files
%config %{_sysconfdir}/cron.hourly/sipwitch
%config %{_initddir}/sipwitch
%config(noreplace) %{_sysconfdir}/logrotate.d/sipwitch
%config(noreplace) %{_sysconfdir}/sipwitch.conf
%config(noreplace) %{_sysconfdir}/sipwitch.d/lab.xml-example
%config(noreplace) %{_sysconfdir}/sipwitch.d/tests.xml
%config(noreplace) %{_sysconfdir}/sysconfig/sipwitch
%{_bindir}/*
%{_sbindir}/sipw
%{_libdir}/%{name}
%{_mandir}/man?/*

%files -n %{libname}
%{_libdir}/libsipwitch.so.%{major}*

%files -n %{devname}
%{_includedir}/sipwitch
%{_libdir}/pkgconfig/libsipwitch.pc
%{_libdir}/libsipwitch.so

