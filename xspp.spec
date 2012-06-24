Summary:	XSLT preprocessor
Summary(pl):	Preprocesor XSLT
Name:		xspp
Version:	0.0.2
Release:	1
License:	BSD
Group:		Applications/Publishing/XML
Vendor:		Michal Moskal <malekith@pld-linux.org>
URL:		http://www.kernel.pl/~malekith/%{name}/
Source0:	http://www.kernel.pl/~malekith/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSPP stands for XSLT Stylesheet PreProcessor. It can be used to
simplify writing XSLT stylesheets. It is result of author being
terrified by xsl:call-template size :)

%description -l pl
XSPP to skr�t od XSLT Stylesheet PreProcessor. Mo�e by� u�yty do
uproszczenia pisania arkuszy styl�w XSLT. Jest wynikiem przera�enia
autora rozmiarem wywo�ania xsl:call-template :)

%prep
%setup -q

%build
%{__make} opt

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html LICENSE
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
