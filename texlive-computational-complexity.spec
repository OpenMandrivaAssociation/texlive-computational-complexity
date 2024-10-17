Name:		texlive-computational-complexity
Version:	44847
Release:	2
Summary:	Class for the journal Computational Complexity
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/computational-complexity
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/computational-complexity.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/computational-complexity.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/computational-complexity.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The LaTeX2e class cc was written for the journal Computational
Complexity, and it can also be used for a lot of other
articles. You may like it since it contains a lot of features
as more intelligent references, a set of theorem definitions,
an algorithm environment, ... The class requires natbib.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/computational-complexity/README
%doc %{_texmfdistdir}/doc/latex/computational-complexity/cc-journals.bib
%{_texmfdistdir}/bibtex/bst/computational-complexity/cc.bst
%{_texmfdistdir}/bibtex/bst/computational-complexity/cc2.bst
%{_texmfdistdir}/tex/latex/computational-complexity/cc-cls.sty
%{_texmfdistdir}/tex/latex/computational-complexity/cc.cls
%{_texmfdistdir}/tex/latex/computational-complexity/cc2cite.sty
%{_texmfdistdir}/tex/latex/computational-complexity/cc4amsart.sty
%{_texmfdistdir}/tex/latex/computational-complexity/cc4apjrnl.sty
%{_texmfdistdir}/tex/latex/computational-complexity/cc4elsart.sty
%{_texmfdistdir}/tex/latex/computational-complexity/cc4jT.sty
%{_texmfdistdir}/tex/latex/computational-complexity/cc4llncs.sty
%{_texmfdistdir}/tex/latex/computational-complexity/cc4siamltex.sty
%{_texmfdistdir}/tex/latex/computational-complexity/cc4svjour.sty
%{_texmfdistdir}/tex/latex/computational-complexity/ccalgo.sty
%{_texmfdistdir}/tex/latex/computational-complexity/ccaux.sty
%{_texmfdistdir}/tex/latex/computational-complexity/cccite.sty
%{_texmfdistdir}/tex/latex/computational-complexity/ccdbs.sty
%{_texmfdistdir}/tex/latex/computational-complexity/cclayout.sty
%{_texmfdistdir}/tex/latex/computational-complexity/ccproof.sty
%{_texmfdistdir}/tex/latex/computational-complexity/ccqed.sty
%{_texmfdistdir}/tex/latex/computational-complexity/ccref.sty
%{_texmfdistdir}/tex/latex/computational-complexity/ccreltx.sty
%{_texmfdistdir}/tex/latex/computational-complexity/ccthm.sty
%{_texmfdistdir}/tex/latex/computational-complexity/relabel.sty
%{_texmfdistdir}/tex/latex/computational-complexity/thcc.sty
%doc %{_texmfdistdir}/doc/latex/computational-complexity/cc-cls-inline.tex
%doc %{_texmfdistdir}/doc/latex/computational-complexity/cc-portability-frame.tex
%doc %{_texmfdistdir}/doc/latex/computational-complexity/cc.pdf
%doc %{_texmfdistdir}/doc/latex/computational-complexity/cc2.dbj
%doc %{_texmfdistdir}/doc/latex/computational-complexity/ccquickref.tex
%doc %{_texmfdistdir}/doc/latex/computational-complexity/cctemplate.tex
#- source
%doc %{_texmfdistdir}/source/latex/computational-complexity/cc.dtx
%doc %{_texmfdistdir}/source/latex/computational-complexity/cc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
