%define module	Hal-Cdroms

Summary:	Access cdroms through HAL and D-Bus
Name:		perl-%{module}
Version:	0.04
Release:	5
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PI/PIXEL/%{module}-%{version}.tar.gz
Buildarch:	noarch
BuildRequires:	perl-devel
Requires:	perl(Net::DBus)
Requires:	udisks

%description
Access cdroms through HAL and D-Bus

%prep
%setup -qn %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes
%{perl_vendorlib}/Hal/Cdroms*
%{_mandir}/man3/*

