Summary:	XSLT preprocessor
Summary(pl.UTF-8):	Preprocesor XSLT
Name:		xspp
Version:	0.0.3
Release:	2
License:	BSD
Group:		Applications/Publishing/XML
Vendor:		Michal Moskal <malekith@pld-linux.org>
Source0:	http://ep09.pld-linux.org/~malekith/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	c5b38f2dfec624bcffb15c14d5d762ba
URL:		http://ep09.pld-linux.org/~malekith/xspp/
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSPP stands for XSLT Stylesheet PreProcessor. It can be used to
simplify writing XSLT stylesheets. It is result of author being
terrified by xsl:call-template size :)

%description -l pl.UTF-8
XSPP to skrót od XSLT Stylesheet PreProcessor. Może być użyty do
uproszczenia pisania arkuszy stylów XSLT. Jest wynikiem przerażenia
autora rozmiarem wywołania xsl:call-template :)

%prep
%setup -q

%build
%{__make} opt

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html LICENSE
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
