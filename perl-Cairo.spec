#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Cairo
Summary:	Perl Cairo bindings
Summary(pl.UTF-8):	Wiązania Cairo dla Perla
Name:		perl-Cairo
Version:	1.041
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	94d8ec38298dbfada0f142455da181d9
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.06
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Number-Delta
%endif
Requires:	cairo >= 1.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides perl access to Cairo library.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do biblioteki Cairo.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Cairo/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%{perl_vendorarch}/Cairo.pm
%dir %{perl_vendorarch}/Cairo
%{perl_vendorarch}/Cairo/Install
%dir %{perl_vendorarch}/auto/Cairo
%attr(755,root,root) %{perl_vendorarch}/auto/Cairo/Cairo.so
%{perl_vendorarch}/auto/Cairo/Cairo.bs
%{_mandir}/man3/Cairo.3pm*
