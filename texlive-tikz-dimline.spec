Name:		texlive-tikz-dimline
Version:	35805
Release:	1
Summary:	Technical dimension lines using PGF/TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-dimline
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-dimline.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-dimline.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
tikz-dimline helps drawing technical dimension lines in TikZ
picture environments. Its usage is similar to some
contributions posted on stackexchange.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-dimline
%doc %{_texmfdistdir}/doc/latex/tikz-dimline

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
