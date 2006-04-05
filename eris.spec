Summary:	A WorldForge client library
Summary(pl):	Biblioteka kliencka WorldForge
Name:		eris
Version:	1.3.8
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
# Source0-md5:	faf7c6d8237af53b93856c356a2de137
URL:		http://www.worldforge.org/dev/eng/libraries/eris
BuildRequires:	Atlas-C++-devel >= 0.5.98
BuildRequires:	skstream-devel >= 0.3.5
BuildRequires:	wfmath-devel >= 0.3.2
BuildRequires:	libsigc++-devel
Requires:	Atlas-C++ >= 0.5.98
Obsoletes:	eris-poll-glib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eris is designed to simplify client development (and avoid repeating
the same work several times), by providing a common system to deal
with the back end tasks.

%description -l pl
Eris zosta³a zaprojektowana w celu uproszczenia zarz±dzania klientem
(i unikniêcia powtarzania tej samej pracy wielokrotnie) poprzez
dostarczenie wspólnego systemu do obslugi zadañ backendu.

%package devel
Summary:	Header files for WorldForge client library
Summary(pl):	Pliki nag³ówkowe biblioteki klienckiej WorldForge
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Atlas-C++-devel
Requires:	skstream-devel
Requires:	wfmath-devel

%description devel
Header files for WorldForge client library.

%description devel -l pl
Pliki nag³ówkowe biblioteki klienckiej WorldForge.

%package static
Summary:	Static WorldForge client library
Summary(pl):	Statyczna biblioteka kliencka WorldForge
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WorldForge client library.

%description static -l pl
Statyczna biblioteka kliencka WorldForge.

%prep
%setup -q

%build
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
