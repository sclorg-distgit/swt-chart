%{?scl:%scl_package swt-chart}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 1

Name:           %{?scl_prefix}swt-chart
Version:        0.10.0
Release:        1.%{baserelease}%{?dist}
Summary:        SWTChart Feature

License:        EPL
URL:            http://www.swtchart.org/
Source0:        http://sourceforge.net/code-snapshots/svn/s/sw/swt-chart/code/swt-chart-code-312-tags-%{version}.zip

BuildArch:      noarch

BuildRequires:  %{?scl_prefix}tycho >= 0.14.0
Requires:       %{?scl_prefix}eclipse-platform >= 3.4.0

%description
SWTChart is a light-weight charting component for SWT.

%package        javadoc
Summary:        Javadoc for %{pkg_name}

%description    javadoc
%{summary}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -q -n %{pkg_name}-code-312-tags-%{version}
# Create the poms
xmvn -o org.eclipse.tycho:tycho-pomgenerator-plugin:generate-poms -DgroupId=org.swtchart
%mvn_package :org.swtchart.example* __noinstall
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%dir %{_mavenpomdir}/swt-chart

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Jul 28 2016 Mat Booth <mat.booth@redhat.com> - 0.10.0-1.1
- Auto SCL-ise package for rh-eclipse46 collection

* Tue Feb 23 2016 Alexander Kurtakov <akurtako@redhat.com> 0.10.0-1
- Update to upstream 0.10 release.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Mat Booth <mat.booth@redhat.com> - 0.9.0-4
- Fix failure to build from source
- Minor spec file clean ups

* Thu Aug 14 2014 Mat Booth <mat.booth@redhat.com> - 0.9.0-3
- Fix unowned directory

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Roland Grunberg <rgrunber@redhat.com> - 0.9.0-1
- Update to 0.9.0 Release.

* Wed Feb 26 2014 Roland Grunberg <rgrunber@redhat.com> - 0.8.0-9
- Change R:java to R:java-headless (Bug 1068558).

* Wed Oct 23 2013 Roland Grunberg <rgrunber@redhat.com> 0.8.0-8
- Fix Bug 1022166.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Roland Grunberg <rgrunber@redhat.com> 0.8.0-5
- Remove deprecated tycho.targetPlatform due to p2 support.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 4 2012 Roland Grunberg <rgrunber@redhat.com> 0.8.0-3
- Use %%{_eclipse_base} from eclipse-platform.

* Mon Apr 2 2012 Roland Grunberg <rgrunber@redhat.com> 0.8.0-2
- Explicitly require java/java-devel >= 1.5 as per manifest.

* Tue Mar 6 2012 Roland Grunberg <rgrunber@redhat.com> 0.8.0-1
- Initial packaging of SWTChart.