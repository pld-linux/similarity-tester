%define		ver	%(echo %{version} | tr . _)
Summary:	Find lexical similarities between files
Summary(pl.UTF-8):	Wyszukiwanie podobieństw leksykalnych pomiędzy plikami
Name:		similarity-tester
Version:	2.26
Release:	0.1
License:	BSD
Group:		Applications/Text
Source0:	http://dickgrune.com/Programs/similarity_tester/sim_%{ver}.zip
# Source0-md5:	089a6d349e1c135db571889a4883c517
URL:		http://dickgrune.com/Programs/similarity_tester/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Find lexical similarities in texts in C, Java, Pascal, Modula-2, Lisp,
Miranda and natural language. This can be used to detect potentially
duplicated code fragments in large software projects and to detect
plagiarism in software and text-based projects.

%description -l pl.UTF-8
Wyszukiwanie podobieństw leksykalnych pomiędzy tekstami w C, Javie,
Pascali, Moduli-2, Lispie, Mirandzie i języku naturalnym. Może być
używane do wykrywania potencjalnie powtarzających się fragmentów kodu
w dużych projektach programistycznych i wykrywania plagiatów w
oprogramowaniu i tekstach.

%prep
%setup -q -c

%build
%{__make} all \
	C_OPT="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

for f in sim_c sim_java sim_lisp sim_m2 sim_mira sim_pasc sim_text ; do
	install -p $f $RPM_BUILD_ROOT%{_bindir}
	echo ".so similarity-tester.1" >$RPM_BUILD_ROOT%{_mandir}/man1/$f.1
done

install sim.1 $RPM_BUILD_ROOT%{_mandir}/man1/similarity-tester.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Answers ChangeLog README.1ST READ_ME TechnReport ToDo sim.html sim.pdf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
