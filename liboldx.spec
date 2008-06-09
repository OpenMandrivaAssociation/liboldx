%define liboldx %mklibname oldx 6
Name: liboldx
Summary:  The oldX Library
Version: 1.0.1
Release: %mkrel 4
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/liboldX-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X.Org X11 liboldX runtime library.

#-----------------------------------------------------------

%package -n %{liboldx}
Summary:  The oldX Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{liboldx}
The oldX Library

#-----------------------------------------------------------

%package -n %{liboldx}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{liboldx} = %{version}
Provides: liboldx-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0

%description -n %{liboldx}-devel
Development files for %{name}

%pre -n %{liboldx}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{liboldx}-devel
%defattr(-,root,root)
%{_libdir}/liboldX.so
%{_libdir}/liboldX.la
%{_libdir}/pkgconfig/oldx.pc
%{_includedir}/X11/X10.h

#-----------------------------------------------------------

%package -n %{liboldx}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{liboldx}-devel = %{version}
Provides: liboldx-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{liboldx}-static-devel
Static development files for %{name}

%files -n %{liboldx}-static-devel
%defattr(-,root,root)
%{_libdir}/liboldX.a

#-----------------------------------------------------------

%prep
%setup -q -n liboldX-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{liboldx}
%defattr(-,root,root)
%{_libdir}/liboldX.so.6
%{_libdir}/liboldX.so.6.0.0


