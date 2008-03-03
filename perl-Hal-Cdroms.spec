%define module	Hal-Cdroms
%define name	perl-%{module}
%define version	0.03
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Access cdroms through HAL and D-Bus
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/P/PI/PIXEL/%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
Requires:	perl(Net::DBus)
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch:	noarch

%description
Access cdroms through HAL and D-Bus

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Hal/Cdroms*
%{_mandir}/*/*


