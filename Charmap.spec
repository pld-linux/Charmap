Summary:	Character map for GNUstep
Name:		Charmap
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://komputilo.org/~crculver/devel/charmap-%{version}.tar.gz
# Source0-md5:	cb3431b5dcb9e7e9c6dfdcc970ee868d
Patch0:		%{name}-initializeWithArguments.patch
URL:		http://www.nongnu.org/charmap
BuildRequires:	gnustep-gui-devel >= 0.9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
Charmap is a powerful character map. It works on Unix-like operating systems with the GNUstep environment installed.

Charmap's power lies its support not just of simply helping to pick characters, but also its display of substantial Unicode data about each character, such as the Unicode name, alias, canonical decomposition, Unicode category, and various representations. With all this, developers and linguaphiles alike will find Charmap a useful tool.

%prep
%setup -q -n charmap-%{version}
%patch0 -p1

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_prefix}/System/Applications/Charmap.app
%attr(755,root,root) %{_prefix}/System/Applications/Charmap.app/Charmap
%dir %{_prefix}/System/Applications/Charmap.app/Resources
%{_prefix}/System/Applications/Charmap.app/Resources/*.desktop
%{_prefix}/System/Applications/Charmap.app/Resources/*.plist
%{_prefix}/System/Applications/Charmap.app/Resources/*.png
%{_prefix}/System/Applications/Charmap.app/Resources/*.gorm
%{_prefix}/System/Applications/Charmap.app/Resources/*.txt
%dir %{_prefix}/System/Applications/Charmap.app/%{gscpu}
%dir %{_prefix}/System/Applications/Charmap.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/Charmap.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Charmap.app/%{gscpu}/%{gsos}/%{libcombo}/Charmap
%{_prefix}/System/Applications/Charmap.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
