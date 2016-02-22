%global debug_package %{nil}

Name:           ocaml-cdrom
Version:        0.9.2
Release:        1%{?dist}
Summary:        Query the state of CDROM devices
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/cdrom
Source0:        https://github.com/xapi-project/cdrom/archive/v%{version}/cdrom-%{version}.tar.gz
BuildRequires:  oasis
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%description
Simple C bindings which allow the state of CDROM devices (and discs
inside) to be queried under Linux.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n cdrom-%{version}

%build
./configure --destdir=%{buildroot} --prefix=%{_prefix}
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs 
make install DESTDIR=%{buildroot}

%files
%doc ChangeLog 
%doc README.md
%{_bindir}/query-cdrom
%{_libdir}/ocaml/cdrom
%exclude %{_libdir}/ocaml/cdrom/*.a
%exclude %{_libdir}/ocaml/cdrom/*.cmxa
%exclude %{_libdir}/ocaml/cdrom/*.cmx
%exclude %{_libdir}/ocaml/cdrom/*.mli
%{_libdir}/ocaml/stublibs/dllcdrom_stubs.so
%{_libdir}/ocaml/stublibs/dllcdrom_stubs.so.owner

%files devel
%{_libdir}/ocaml/cdrom/*.a
%{_libdir}/ocaml/cdrom/*.cmx
%{_libdir}/ocaml/cdrom/*.cmxa
%{_libdir}/ocaml/cdrom/*.mli

%changelog
* Fri Feb 05 2016 Euan Harris <euan.harris@citrix.com> - 0.9.2-1
- Switch to Oasis

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.1-3
- Split files correctly between base and devel packages

* Tue May 28 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.1-2
- Initial package

