#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pnam	Cairo
Summary:	Perl Cairo bindings
Summary(pl.UTF-8):	Wiązania Cairo dla Perla
Name:		perl-Cairo
Version:	1.106
Release:	6
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	47ca0ae0f5b9bc4c16a27627ff48bd8b
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.06
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Number-Delta >= 1.0
%endif
Requires:	cairo >= 1.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides perl access to Cairo library.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do biblioteki Cairo.

%package devel
Summary:	Development files for Perl Cairo bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Cairo dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.10.0

%description devel
Development files for Perl Cairo bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Cairo dla Perla.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Cairo/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%{perl_vendorarch}/Cairo.pm
%dir %{perl_vendorarch}/Cairo
%dir %{perl_vendorarch}/auto/Cairo
%attr(755,root,root) %{perl_vendorarch}/auto/Cairo/Cairo.so
%{_mandir}/man3/Cairo.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Cairo/Install
