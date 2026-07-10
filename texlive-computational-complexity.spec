%global tl_name computational-complexity
%global tl_revision 44847

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.25f
Release:	%{tl_revision}.1
Summary:	Class for the journal Computational Complexity
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/computational-complexity
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/computational-complexity.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/computational-complexity.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/computational-complexity.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The LaTeX2e class cc was written for the journal Computational
Complexity, and it can also be used for a lot of other articles. You may
like it since it contains a lot of features such as more intelligent
references, a set of theorem definitions, an algorithm environment, and
more. The class requires natbib.

