Name:           ocaml-flock
Version:        1.0.0
Release:        1%{?dist}
Summary:        OCaml bindings to flock(2)
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/simonjbeaumont/ocaml-flock
Source0:        https://github.com/simonjbeaumont/ocaml-flock/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  libffi-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-ctypes-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  oasis

%description
OCaml bindings to flock(2).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libffi%{?_isa}
Requires:       ocaml-ctypes-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install

%check
./configure --enable-tests
make test

%files
%doc README.md
%doc LICENSE
%{_libdir}/ocaml/flock
%{_libdir}/ocaml/flock_bindings
%{_libdir}/ocaml/stublibs/dllflock_stubs.so
%{_libdir}/ocaml/stublibs/dllflock_stubs.so.owner
%exclude %{_libdir}/ocaml/flock/*.a
%exclude %{_libdir}/ocaml/flock/*.cmxa
%exclude %{_libdir}/ocaml/flock/*.mli
%exclude %{_libdir}/ocaml/flock_bindings/*.a
%exclude %{_libdir}/ocaml/flock_bindings/*.cmxa

%files devel
%{_libdir}/ocaml/flock/*.a
%{_libdir}/ocaml/flock/*.cmxa
%{_libdir}/ocaml/flock/*.mli
%{_libdir}/ocaml/flock_bindings/*.a
%{_libdir}/ocaml/flock_bindings/*.cmxa

%changelog
* Mon Nov 9 2015 Si Beaumont <simon.beaumont@citrix.com> - 1.0.0-1
- Initial package
