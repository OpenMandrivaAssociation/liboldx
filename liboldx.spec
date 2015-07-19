%define	major	6
%define libname	%mklibname oldx %{major}
%define devname	%mklibname oldx -d

Summary:	The oldX Library
Name:		liboldx
Version:	1.0.1
Release:	19
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/liboldX-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
X.Org X11 liboldX runtime library.

%package -n %{libname}
Summary:	The oldX Library
Group:		Development/X11
Provides:	%{name} = %{version}

%description -n %{libname}
The oldX Library

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}oldx6-devel < 1.0.1-11
Obsoletes:	%{_lib}oldx6-static-devel < 1.0.1-11

%description -n %{devname}
Development files for %{name}

%pre -n %{devname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%prep
%setup -qn liboldX-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/liboldX.so.%{major}*

%files -n %{devname}
%{_libdir}/liboldX.so
%{_libdir}/pkgconfig/oldx.pc
%{_includedir}/X11/X10.h

