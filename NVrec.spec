Summary:	New Video Recorder
Name:		NVrec
Version:	20010808
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-avifile-0.6.patch
Patch1:		%{name}-make.patch
Requires:	divx4linux >= 20010824
Requires:	avifile >= 0.6-0.20010809
Requires:	rte
Requires:	lame-libs >= 3.70
BuildRequires:  lame-libs-static >= 3.70
BuildRequires:	avifile-devel >= 0.6-0.20010809
BuildRequires:  divx4linux-devel >= 20010824
BuildRequires:	rte-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
NuppelVideo is a simple low consuming and fast capture program
for bttv-cards (BT8x8) it is based on the RTjpeg2.0 test3* programs
from Justin Schoemann , who wrote the very fast and fine RTjpeg2.0
codec (improved by Joerg Walter and Wim Taymans).

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
libtoolize --copy --force
aclocal
automake
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS COPYING INSTALL README CREDITS ChangeLog KNOWN_BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%doc *.gz
