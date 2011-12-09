# revision 24792
# category Package
# catalog-ctan /macros/latex/contrib/silence
# catalog-date 2011-12-06 22:18:19 +0100
# catalog-license lppl
# catalog-version 1.4
Name:		texlive-silence
Version:	1.4
Release:	1
Summary:	Selective filtering of error messages and warnings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/silence
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/silence.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/silence.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/silence.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to filter out unwanted warnings and
error messages issued by LaTeX, packages and classes, so they
won't pop out when there's nothing one can do about them.
Filtering goes from the very broad ("avoid all messages by such
and such") to the fine-grained ("avoid messages that begin
with..."). Messages may be saved to an external file for later
reference.

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/silence/silence.sty
%doc %{_texmfdistdir}/doc/latex/silence/README
%doc %{_texmfdistdir}/doc/latex/silence/silence-doc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/silence/silence-doc.dtx
%doc %{_texmfdistdir}/source/latex/silence/silence.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
