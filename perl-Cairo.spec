#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Cairo
Summary:	Perl Cairo bindings
Summary(pl):	Wi�zania Cairo dla Perla
Name:		perl-Cairo
Version:	1.021
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	72696240a9ba97694209d0a0c7367b57
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	cairo-devel >= 1.2.4
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.06
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides perl access to Cairo library.

%description -l pl
Ten modu� daje dost�p z poziomu Perla do biblioteki Cairo.

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
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/Cairo
%{perl_vendorarch}/Cairo/Install
%dir %{perl_vendorarch}/auto/Cairo
%attr(755,root,root) %{perl_vendorarch}/auto/Cairo/Cairo.so
%{perl_vendorarch}/auto/Cairo/Cairo.bs
%{_mandir}/man3/*
