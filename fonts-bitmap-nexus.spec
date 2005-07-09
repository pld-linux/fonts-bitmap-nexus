Summary:	A sans-serif fixed font
%define	_pkgname	nexus
Name:		fonts-bitmap-nexus
Version:	0.0.2
%define	_snap	20050704
# this is not changing so don't include snap in rel
Release:	0.1
License:	BSD
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/enlightenment/%{_pkgname}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/snaps/enli/misc/%{_pkgname}-%{_snap}.tar.gz
# Source0-md5:	0c430037a88e7d986da8bfda227c061a
URL:		http://enlightenment.org/
BuildRequires:	XFree86-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A sans-serif, fixed font with iso8859 encoding. Only available as 10
point with medium weight.

%prep
%setup -q -n %{_pkgname}

%build
/usr/bin/X11/bdftopcf nex6x10.bdf > nex6x10.pcf
gzip -9nf nex6x10.pcf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_fontsdir}
install nex6x10.pcf.gz $RPM_BUILD_ROOT%{_fontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%{_fontsdir}/nex6x10.pcf.gz