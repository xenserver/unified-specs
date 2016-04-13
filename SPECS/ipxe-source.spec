%define src_name ipxe

Summary: iPXE source archive
Name: ipxe-source
Version: 1
Release: 1
License: GPLv2
Source0: http://hg.uk.xensource.com/git/carbon/trunk-ring0/ipxe.git/snapshot/refs/heads/master#/%{src_name}.tar.gz
BuildArch: noarch

%description
Ipxe specfile

%prep
%setup -n %{src_name}-%{version}

%build
mkdir -p ../%{src_name}
find . | cpio -pdmv ../%{src_name}

%install
mkdir -p %{buildroot}/usr/src
tar zcvf %{buildroot}/usr/src/%{name}.tar.gz -C .. %{src_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/src/%{name}.tar.gz
