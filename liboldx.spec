%define liboldx %mklibname oldx 6
Name: liboldx
Summary:  The oldX Library
Version: 1.0.1
Release: %mkrel 9
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




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-9mdv2011.0
+ Revision: 661511
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-8mdv2011.0
+ Revision: 602591
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-7mdv2010.1
+ Revision: 520894
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-6mdv2010.0
+ Revision: 425656
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-5mdv2009.0
+ Revision: 222944
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2008.1
+ Revision: 150739
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-16 23:54:45 (27471)
- better(?) description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

