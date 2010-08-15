Summary:	Utilities to read/write MSR CPU registers
Summary(pl.UTF-8):	Narzędzia do odczytu i zapisu rejestrów MSR procesora
Name:		msr-tools
Version:	1.2
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/cpu/msr-tools/%{name}-%{version}.tar.bz2
# Source0-md5:	309b6514992817d6b5ca8e3887be0f9b
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities to read/write MSR CPU registers.

%description -l pl.UTF-8
Narzędzia do odczytu i zapisu rejestrów MSR procesora.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -fomit-frame-pointer -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	sbindir=$RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rdmsr
%attr(755,root,root) %{_sbindir}/wrmsr
