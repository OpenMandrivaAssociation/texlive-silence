# revision 27028
# category Package
# catalog-ctan /macros/latex/contrib/silence
# catalog-date 2012-07-04 10:43:54 +0200
# catalog-license lppl
# catalog-version 1.5b
Name:		texlive-silence
Version:	1.5b
Release:	9
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

%post
    %{_sbindir}/texlive.post

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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5b-1
+ Revision: 812860
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-3
+ Revision: 770278
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-2
+ Revision: 756025
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 739875
- texlive-silence

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 719535
- texlive-silence
- texlive-silence
- texlive-silence
- texlive-silence

