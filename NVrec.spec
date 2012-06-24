Summary:	New Video Recorder
Summary(pl):	Nowy Rejestrator Obrazu
Name:		NVrec
Version:	20020710
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://nvrec.sourceforge.net/downloads/nvrec-%{version}.tar.gz
#Patch0:		%{name}-avifile-0.6.patch
#Patch1:		%{name}-make.patch
URL:		http://nvrec.sf.net/
Requires:	divx4linux >= 20010824
Requires:	avifile >= 0.6-0.20010809.2
Requires:	rte
Requires:	lame-libs >= 3.70
BuildRequires:  lame-libs-static >= 3.70
BuildRequires:	avifile-devel >= 0.6-0.20010809.2
BuildRequires:  divx4linux-devel >= 20010824
BuildRequires:	rte-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
NewVideoRecorder is a high quality video capture toolkit for Linux.
It includes deep buffering of audio and video to reduce frame dropping,
a smooth dropping algorithm to keep the video smooth if dropping is
required, and dynamic stretching of the audio stream to exactly match
the video stream. It can use v4l1 and v4l2 devices as video sources,
and OSS devices as an audio source. It can produce QuickTime, AVI,
NuppelVideo 0.4 files, and MPEG-1 files.

%description -l pl
NewVideoRecorder to narz�dzie wysokiej jako�ci do zgrywania obrazu dla
Linuksa. U�ywa du�ych bufor�w d�wi�ku i obrazu, aby zmniejszy� gubienie
ramek, algorytmu p�ynnego pomijania ramek, aby utrzyma� p�ynno�� obrazu
kiedy ramk� trzeba pomin�� i dynamiczne rozci�ganie strumienia d�wi�ku
aby zgadza� si� ze strumieniem obrazu. Mo�e u�ywa� urz�dze� v4l1 i v4l2
jako �r�d�e� obrazu i urz�dze� OSS jako �r�de� d�wi�ku. Mo�e zapisywa�
pliki QuickTime, AVI, NuppelVideo 0.4 i MPEG-1.

%prep
%setup  -q -n nvrec-%{version}
#%patch0 -p1
#%patch1 -p1

%build
./bootstrap
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
%doc *.gz
