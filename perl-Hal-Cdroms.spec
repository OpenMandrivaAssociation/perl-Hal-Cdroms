%define module	Hal-Cdroms

Name:		perl-%{module}
Version:	0.03
Release:	9
Summary:	Access cdroms through HAL and D-Bus
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/P/PI/PIXEL/%{module}-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
Requires:	perl(Net::DBus)

BuildArch:	noarch

%description
Access cdroms through HAL and D-Bus

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes
%{perl_vendorlib}/Hal/Cdroms*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.03-8mdv2012.0
+ Revision: 765299
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.03-7
+ Revision: 763840
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.03-6
+ Revision: 763067
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.03-5
+ Revision: 667208
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.03-4mdv2010.1
+ Revision: 426511
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.03-3mdv2009.1
+ Revision: 351964
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.03-2mdv2009.0
+ Revision: 223784
- rebuild

* Mon Mar 03 2008 Pixel <pixel@mandriva.com> 0.03-1mdv2008.1
+ Revision: 178078
- 0.03:
- ->mount and ->umount now work even the cdrom is listed in fstab,
  use ->mount_hal and ->umount_hal if you want the HAL restriction

* Fri Feb 29 2008 Pixel <pixel@mandriva.com> 0.02-1mdv2008.1
+ Revision: 176782
- 0.02:
- save error in $hal_cdroms->{error}
- ->mount: do not set the mount point, HAL handles it

* Thu Feb 28 2008 Pixel <pixel@mandriva.com> 0.01-1mdv2008.1
+ Revision: 176557
- fix BuildRequires and add BuildRoot
- initial release
- create perl-Hal-Cdroms

