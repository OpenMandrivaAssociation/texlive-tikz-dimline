%global tl_name tikz-dimline
%global tl_revision 35805

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Technical dimension lines using PGF/TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-dimline
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-dimline.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-dimline.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
tikz-dimline helps drawing technical dimension lines in TikZ picture
environments. Its usage is similar to some contributions posted on
stackexchange.

