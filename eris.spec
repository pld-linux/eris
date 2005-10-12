Summary:	A WorldForge client library.
Name:		eris
Version:	1.3.8
Release:	0.1
License:	GPL
Group:		Libraries
URL:		http://www.worldforge.org/dev/eng/libraries/eris
Source0:	http://dl.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
# Source0-md5:	faf7c6d8237af53b93856c356a2de137
BuildRequires:	Atlas-C++-devel >= 0.5.98
BuildRequires:	wfmath-devel >= 0.3.2
BuildRequires:	skstream-devel >= 0.3.5
Requires:	Atlas-C++ >= 0.5.98
Obsoletes:	eris-poll-glib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eris is designed to simplify client development (and avoid repeating
the same work several times), by providing a common system to deal
with the back end tasks.

%package devel
Summary:	A WorldForge client library headers and static libs.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Atlas-C++-devel
Requires:	wfmath-devel
Requires:	skstream-devel

%description devel
Eris is designed to simplify client development (and avoid repeating
the same work several times), by providing a common system to deal
with the back end tasks.

%prep
%setup -q

%build
CXXFLAGS=%{rpmcflags}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*
%doc AUTHORS COPYING NEWS README

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/lib*.a
%{_pkgconfigdir}/*
%{_includedir}/*
