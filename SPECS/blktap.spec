Summary: blktap user space utilities
Name: blktap
Version: 3.2.0
Release: xs7777
License: GPLv2 or BSD
Group: System/Hypervisor
Source0: http://hg.uk.xensource.com/git/carbon/trunk-transformer/blktap.git/snapshot/refs/heads/master#/blktap.tar.bz2

Patch1: blktap-udev-ignore-tapdevs.patch
BuildRoot: %{_tmppath}/%{name}-%{release}-buildroot
Obsoletes: xen-blktap
BuildRequires: e2fsprogs-devel, libaio-devel, systemd, autogen, autoconf, automake, libtool, libuuid-devel
BuildRequires: xen-devel, kernel-devel, xen-dom0-libs-devel, zlib-devel, xen-libs-devel
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Blktap creates kernel block devices which realize I/O requests to
processes implementing virtual hard disk images entirely in user
space.

Typical disk images may be implemented as files, in memory, or
stored on other hosts across the network. The image drivers included
with tapdisk can map disk I/O to sparse file images accessed through
Linux DIO/AIO and VHD images with snapshot functionality.

This packages includes the control utilities needed to create
destroy and manipulate devices ('tap-ctl'), the 'tapdisk' driver
program to perform tap devices I/O, and a number of image drivers.

%package devel
Summary: BlkTap Development Headers and Libraries
Requires: blktap = %{version}
Group: Development/Libraries
Obsoletes: xen-blktap

%description devel
Blktap and VHD development files.

%prep
%setup -q
%patch1 -p1

%build
sh autogen.sh
%configure
%{?cov_wrap} make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_localstatedir}/log/blktap

%files
%defattr(-,root,root,-)
%doc
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_bindir}/vhd-util
%{_bindir}/vhd-update
%{_bindir}/vhd-index
%{_bindir}/tapback
%{_bindir}/cpumond
%{_sbindir}/lvm-util
%{_sbindir}/tap-ctl
%{_sbindir}/td-util
%{_sbindir}/td-rated
%{_sbindir}/part-util
%{_sbindir}/vhdpartx
%{_sbindir}/thinprovd
%{_sbindir}/thin-cli
%{_sbindir}/xlvhd-resize
%{_sbindir}/xlvhd-refresh
%{_libexecdir}/tapdisk
%{_sysconfdir}/udev/rules.d/blktap.rules
%{_sysconfdir}/logrotate.d/blktap
%{_sysconfdir}/xensource/bugtool/tapdisk-logs.xml
%{_sysconfdir}/xensource/bugtool/tapdisk-logs/description.xml
%{_sysconfdir}/rc.d/init.d/thinprovd
%{_localstatedir}/log/blktap
%{_unitdir}/tapback.service
%{_unitdir}/cpumond.service

%files devel
%defattr(-,root,root,-)
%doc
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/vhd/*
%{_includedir}/blktap/*

%post
%systemd_post tapback.service
[ ! -x /sbin/chkconfig ] || chkconfig --add thinprovd
%systemd_post cpumond.service

%preun
%systemd_preun tapback.service
%systemd_preun cpumond.service

%postun
%systemd_postun tapback.service
%systemd_postun cpumond.service

%changelog
