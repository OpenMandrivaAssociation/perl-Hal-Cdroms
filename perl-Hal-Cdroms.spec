%define module	Hal-Cdroms

Name:		perl-%{module}
Version:	0.04
Release:	2
Summary:	Access cdroms through HAL and D-Bus
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PI/PIXEL/%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
Requires:	perl(Net::DBus)
Requires:	udisks
BuildRequires:	perl-devel
Buildarch:	noarch

%description
Access cdroms through HAL and D-Bus

%prep
%setup -q -n %{module}-%{version}

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
%{_mandir}/*/*
