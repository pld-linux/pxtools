Summary:	Utility for Paradox databases
Summary(pl.UTF-8):   Narzędzie do baz danych Paradox
Name:		pxtools
Version:	0.0.20
Release:	1
License:	GPL
Group:		Applications/Databases/Interfaces
Source0:	http://jan.kneschke.de/projects/pxtools/download/%{name}-%{version}.tar.gz
# Source0-md5:	c68ee33366446bdcd7ab1852b15f98e5
URL:		http://jan.kneschke.de/projects/pxtools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pxtools is a collection of tools to work with Paradox databases. It
consists of pxinfo and dump-utilities to generate SQL, CSV, and XML
from the database. The pxtools are able to convert all versions of
Paradox databases and even support the external MEMO-Blobs.

%description -l pl.UTF-8
pxtools to zestaw narzędzi do pracy z bazami danych Paradox. Składa
się z pxinfo oraz narzędzi do zrzucania baz do generowania plików SQL,
CSV i XML z baz danych. pxtools potrafią konwertować wszystkie wersje
baz danych Paradox, a nawet wspierają zewnętrzne bloby MEMO.

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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
