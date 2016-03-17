%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-pa-structural-sexp
Version:        112.35.00
Release:        1%{?dist}
Summary:        Jane Street's pa_structural_sexp

Group:          Development/Libraries
License:        Apache Software License 2.0
URL:            https://github.com/janestreet/pa_structural_sexp
Source0:        https://ocaml.janestreet.com/ocaml-core/112.35/files/pa_structural_sexp-%{version}.tar.gz

ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-type-conv

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh


%description
Jane Street's pa_structural_sexp.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n pa_structural_sexp-%{version}

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
%doc LICENSE.txt INRIA-DISCLAIMER.txt
%{_libdir}/ocaml/pa_structural_sexp
%if %opt
%exclude %{_libdir}/ocaml/pa_structural_sexp/*.a
%exclude %{_libdir}/ocaml/pa_structural_sexp/*.cmxa
%endif
%exclude %{_libdir}/ocaml/pa_structural_sexp/*.mli


%files devel
%defattr(-,root,root,-)
%doc LICENSE.txt INRIA-DISCLAIMER.txt
%if %opt
%{_libdir}/ocaml/pa_structural_sexp/*.a
%{_libdir}/ocaml/pa_structural_sexp/*.cmxa
%endif
%{_libdir}/ocaml/pa_structural_sexp/*.mli

%changelog
* Thu Nov 12 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 112.35.00-1
- Initial package
