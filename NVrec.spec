Summary:	New Video Recorder
Summary(pl.UTF-8):	Nowy Rejestrator Obrazu
Name:		NVrec
Version:	20030316
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://nvrec.sourceforge.net/downloads/nvrec-%{version}.tar.gz
# Source0-md5:	82a7f0f3e661bb2740cb3778edd1dfae
#Patch0:	%{name}-avifile-0.6.patch
#Patch1:	%{name}-make.patch
URL:		http://nvrec.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel >= 1:0.6-0.20010809.2
BuildRequires:	divx4linux-devel >= 20010824
BuildRequires:	lame-libs-static >= 3.70
BuildRequires:	libtool
BuildRequires:	rte-devel
Requires:	avifile >= 1:0.6-0.20010809.2
Requires:	divx4linux >= 20010824
Requires:	lame-libs >= 3.70
Requires:	rte
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NewVideoRecorder is a high quality video capture toolkit for Linux. It
includes deep buffering of audio and video to reduce frame dropping, a
smooth dropping algorithm to keep the video smooth if dropping is
required, and dynamic stretching of the audio stream to exactly match
the video stream. It can use v4l1 and v4l2 devices as video sources,
and OSS devices as an audio source. It can produce QuickTime, AVI,
NuppelVideo 0.4 files, and MPEG-1 files.

%description -l pl.UTF-8
NewVideoRecorder to narzędzie wysokiej jakości do zgrywania obrazu dla
Linuksa. Używa dużych buforów dźwięku i obrazu, aby zmniejszyć
gubienie ramek, algorytmu płynnego pomijania ramek, aby utrzymać
płynność obrazu kiedy ramkę trzeba pominąć i dynamiczne rozciąganie
strumienia dźwięku aby zgadzał się ze strumieniem obrazu. Może używać
urządzeń v4l1 i v4l2 jako źródeł obrazu i urządzeń OSS jako źródeł
dźwięku. Może zapisywać pliki QuickTime, AVI, NuppelVideo 0.4 i
MPEG-1.

%prep
%setup  -q -n nvrec-%{version}
#%%patch0 -p1
#%%patch1 -p1

%build
./bootstrap
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog FAQ KNOWN_BUGS NEWS README STATUS
%attr(755,root,root) %{_bindir}/*
