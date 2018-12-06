#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-MultiPartParser
Version  : 0.02
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/HTTP-MultiPartParser-0.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/HTTP-MultiPartParser-0.02.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhttp-multipartparser-perl/libhttp-multipartparser-perl_0.02-1.debian.tar.xz
Summary  : 'HTTP MultiPart Parser'
Group    : Development/Tools
License  : Artistic-1.0-Perl
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

%description dev
dev components for the perl-HTTP-MultiPartParser package.


%prep
%setup -q -n HTTP-MultiPartParser-0.02
cd ..
%setup -q -T -D -n HTTP-MultiPartParser-0.02 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/HTTP-MultiPartParser-0.02/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.28.1HTTP/MultiPartParser.pm
/usr/lib/perl5/vendor_perl/5.28.1HTTP/MultiPartParser.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::MultiPartParser.3
