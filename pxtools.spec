Summary:	Utility for paradox databases
Summary(pl):	Narzêdzie do manipulowania bazami danych Paradox
Name:		pxtools
Version:	0.0.20
Release:	1
License:	GPL
Group:		Applications/Databases/Interfaces
Source0:	http://jan.kneschke.de/projects/pxtools/download/%{name}-%{version}.tar.gz
URL:		http://jan.kneschke.de/projects/pxtools/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pxtools is a collection of tools to work with Paradox databases. It
consists of pxinfo and dump-utilities to generate SQL, CSV, and XML
from the database. The pxtools are able to convert all versions of
Paradox databases and even support the external MEMO-Blobs

%description -l pl
empty

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_datadir}/locale/de/LC_MESSAGES/pxtools.mo
