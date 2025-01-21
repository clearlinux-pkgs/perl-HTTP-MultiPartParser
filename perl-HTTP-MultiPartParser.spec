#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-MultiPartParser
Version  : 0.02
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/HTTP-MultiPartParser-0.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/HTTP-MultiPartParser-0.02.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhttp-multipartparser-perl/libhttp-multipartparser-perl_0.02-1.debian.tar.xz
Summary  : 'HTTP MultiPart Parser'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-MultiPartParser-license = %{version}-%{release}
Requires: perl-HTTP-MultiPartParser-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Deep)

%description
NAME
HTTP::MultiPartParser - HTTP MultiPart Parser
SYNOPSIS
$parser = HTTP::MultiPartParser->new(
boundary  => $boundary,
on_header => $on_header,
on_body   => $on_body,
);

while ($octets = read_octets_from_body()) {
$parser->parse($octets);
}

$parser->finish;

%package dev
Summary: dev components for the perl-HTTP-MultiPartParser package.
Group: Development
Provides: perl-HTTP-MultiPartParser-devel = %{version}-%{release}
Requires: perl-HTTP-MultiPartParser = %{version}-%{release}

%description dev
dev components for the perl-HTTP-MultiPartParser package.


%package license
Summary: license components for the perl-HTTP-MultiPartParser package.
Group: Default

%description license
license components for the perl-HTTP-MultiPartParser package.


%package perl
Summary: perl components for the perl-HTTP-MultiPartParser package.
Group: Default
Requires: perl-HTTP-MultiPartParser = %{version}-%{release}

%description perl
perl components for the perl-HTTP-MultiPartParser package.


%prep
%setup -q -n HTTP-MultiPartParser-0.02
cd %{_builddir}
tar xf %{_sourcedir}/libhttp-multipartparser-perl_0.02-1.debian.tar.xz
cd %{_builddir}/HTTP-MultiPartParser-0.02
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/HTTP-MultiPartParser-0.02/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-MultiPartParser
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-HTTP-MultiPartParser/86a29cd3c0f33b096764475c24e17cc0c001f617
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::MultiPartParser.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-MultiPartParser/86a29cd3c0f33b096764475c24e17cc0c001f617

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
