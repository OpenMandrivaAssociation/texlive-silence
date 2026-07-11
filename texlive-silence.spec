%global tl_name silence
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5b
Release:	%{tl_revision}.1
Summary:	Selective filtering of error messages and warnings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/silence
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/silence.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/silence.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/silence.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the user to filter out unwanted warnings and error
messages issued by LaTeX, packages and classes, so they won't pop out
when there's nothing one can do about them. Filtering goes from the very
broad ("avoid all messages by such and such") to the fine-grained
("avoid messages that begin with..."). Messages may be saved to an
external file for later reference.

