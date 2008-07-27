%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	HCE_SHA
Summary:	Crypt::HCE_SHA Perl module - hash chaining encryption using SHA
Summary(pl.UTF-8):	Moduł Perla Crypt::HCE_SHA - łańcuchowe kodowanie z użyciem SHA
Name:		perl-Crypt-HCE_SHA
Version:	0.70
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c18dc95cd5ce92828c6e4efdf07fa7a9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-MIME-Base64 >= 2
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-MIME-Base64 >= 2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a chaining block cipher using a one way hash.
This method of encryption is the same that is used by radius (RFC2138)
and is also described in Applied Cryptography.

%description -l pl.UTF-8
Ten moduł jest implementacją łańcuchowego szyfru blokowego przy użyciu
jednokierunkowego mieszania. Jest to ta sama metoda, co używana w
radiusie (RFC 2138) oraz opisana w Applied Cryptography.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/HCE_SHA.pm
%{perl_vendorlib}/auto/Crypt/HCE_SHA
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
