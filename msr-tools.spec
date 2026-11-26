Summary:	Utilities to read/write MSR CPU registers
Summary(pl.UTF-8):	Narzędzia do odczytu i zapisu rejestrów MSR procesora
Name:		msr-tools
Version:	1.3
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://github.com/intel/msr-tools/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	649a093ba55fbbb5cc0fa64b995667e0
ExclusiveArch:	%{ix86} %{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities to read/write MSR CPU registers.

%description -l pl.UTF-8
Narzędzia do odczytu i zapisu rejestrów MSR procesora.

%prep
%setup -q -n %{name}-%{name}-%{version}

# cpuid from upstream is shipped by the cpuid package
%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -fomit-frame-pointer -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64" \
	LDFLAGS="%{rpmldflags}" \
	BIN="rdmsr wrmsr"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	BIN="rdmsr wrmsr"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rdmsr
%attr(755,root,root) %{_sbindir}/wrmsr
