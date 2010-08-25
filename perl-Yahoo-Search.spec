%define upstream_name    Yahoo-Search
%define upstream_version 1.11.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Interface to Yahoo!s Search API
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Yahoo/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Encode)
BuildRequires: perl(LWP)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The XML sent back from Yahoo! is fairly simple, and is guaranteed to be
well formed, so we really don't need much more than to make the data easily
available. I'd like to use XML::Simple, but it uses XML::Parser, which
suffers from crippling memory leaks (in one test, 36k was lost with each
parsing of a 7k xml file), so I've rolled my own simple version that might
be called, uh, XML::SuperDuperSimple.

The end result is identical to what XML::Simple would produce, at least for
the XML the Yahoo! sends back. It may well be useful for other things that
use a similarly small subset of XML notation.

This package is also much faster than XML::Simple / XML::Parser, producing
the same output 41 times faster, in my tests. That's the benefit of not
having to handle everything, I guess.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%perl_vendorlib/*


