%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-async-rpc-kernel
Version:        112.35.00
Release:        1%{?dist}
Summary:        Platform-independent core of Async RPC library

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/async_rpc_kernel
Source0:        https://ocaml.janestreet.com/ocaml-core/112.35/individual/async_rpc_kernel-%{version}.tar.gz
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-async-kernel-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-bin-prot-devel
BuildRequires:  ocaml-core-kernel-devel
BuildRequires:  ocaml-fieldslib-devel
BuildRequires:  ocaml-pa-ounit-devel
BuildRequires:  ocaml-pa-test-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-herelib-devel
BuildRequires:  ocaml-comparelib-devel
BuildRequires:  ocaml-custom-printf-devel

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
Part of Jane Street’s Core library
The Core suite of libraries is an industrial strength alternative to
OCaml's standard library that was developed by Jane Street, the
largest industrial user of OCaml.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:  ocaml-bin-prot-devel
Requires:  ocaml-core-kernel-devel
Requires:  ocaml-fieldslib-devel
Requires:  ocaml-pa-ounit-devel
Requires:  ocaml-pa-test-devel
Requires:  ocaml-sexplib-devel
Requires:  ocaml-herelib-devel
Requires:  ocaml-comparelib-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n async_rpc_kernel-%{version}

%build
ocaml setup.ml -configure --prefix %{_prefix} \
      --libdir %{_libdir} \
      --libexecdir %{_libexecdir} \
      --exec-prefix %{_exec_prefix} \
      --bindir %{_bindir} \
      --sbindir %{_sbindir} \
      --mandir %{_mandir} \
      --datadir %{_datadir} \
      --localstatedir %{_localstatedir} \
      --sharedstatedir %{_sharedstatedir} \
      --destdir $RPM_BUILD_ROOT
ocaml setup.ml -build


%check
ocaml setup.ml -test


%install
rm -rf $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocaml setup.ml -install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt THIRD-PARTY.txt INRIA-DISCLAIMER.txt
%{_libdir}/ocaml/async_rpc_kernel
%if %opt
%exclude %{_libdir}/ocaml/async_rpc_kernel/*.a
%exclude %{_libdir}/ocaml/async_rpc_kernel/*.cmxa
%endif
%exclude %{_libdir}/ocaml/async_rpc_kernel/*.ml
%exclude %{_libdir}/ocaml/async_rpc_kernel/*.mli

%files devel
%defattr(-,root,root,-)
%doc LICENSE.txt THIRD-PARTY.txt INRIA-DISCLAIMER.txt
%if %opt
%{_libdir}/ocaml/async_rpc_kernel/*.a
%{_libdir}/ocaml/async_rpc_kernel/*.cmxa
%endif
%{_libdir}/ocaml/async_rpc_kernel/*.ml
%{_libdir}/ocaml/async_rpc_kernel/*.mli

%changelog
* Thu Nov 12 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 112.35.00-1
- Initial package
