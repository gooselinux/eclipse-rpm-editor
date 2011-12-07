%define eclipse_base        %{_libdir}/eclipse
%define install_loc         %{_datadir}/eclipse/dropins
%define qualifier           201003171651

Name:           eclipse-rpm-editor
Version:        0.5.0
Release:        2%{?dist}
Summary:        RPM Specfile editor for Eclipse
Group:          Development/Tools
License:        EPL
URL:            http://www.eclipse.org/linuxtools/
# This tarball was made using the included script, like so:
#   sh ./fetch-specfile-editor.sh %{tag_name} %{version}
Source0:        specfile-editor-fetched-src-%{version}.tar.bz2
Source1:        fetch-specfile-editor.sh
Patch0:         rpmtools-refresh.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: java-devel >= 1.5.0
BuildRequires: eclipse-pde >= 1:3.3.0
BuildRequires: eclipse-changelog >= 2.5.1
Requires: eclipse-platform >= 3.3.1
Requires: eclipse-changelog >= 2.5.1
Requires: rpmlint >= 0.81
Requires: rpmdevtools

# These plugins are really noarch but the changelog plugin need cdt which
# we only build on these architectures.
ExclusiveArch: %{ix86} x86_64 
%define debug_package %{nil}

%description
The Eclipse Specfile Editor package contains Eclipse plugins that are
useful for maintenance of RPM specfiles within the Eclipse IDE.

%prep
%setup -q -n specfile-editor-fetched-src-%{version}

pushd org.eclipse.linuxtools.rpm.ui.editor
%patch0
popd

%build
%{eclipse_base}/buildscripts/pdebuild -a "-DforceContextQualifier=%{qualifier} -DjavacSource=1.5 -DjavacTarget=1.5" \
 -f  org.eclipse.linuxtools.rpm
%{eclipse_base}/buildscripts/pdebuild -a "-DforceContextQualifier=%{qualifier} -DjavacSource=1.5 -DjavacTarget=1.5" \
 -f  org.eclipse.linuxtools.rpm.ui.editor -d changelog ;

%install
rm -rf %{buildroot}
installDir=%{buildroot}%{install_loc}/rpm-editor
install -d -m 755 $installDir
unzip -q -d $installDir \
 build/rpmBuild/org.eclipse.linuxtools.rpm.ui.editor.zip
unzip -q -d $installDir \
 build/rpmBuild/org.eclipse.linuxtools.rpm.zip

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc org.eclipse.linuxtools.rpm.ui.editor-feature/*.html
%{install_loc}/rpm-editor

%changelog
* Fri Apr 9 2010 Alexander Kurtakov <akurtako@redhat.com> 0.5.0-2
- Add patch to dinamically refresh package completion based on the tool selected.

* Mon Mar 22 2010 Alexander Kurtakov <akurtako@redhat.com> 0.5.0-1.1
- Rebase to Linux Tools 0.5 release.

* Mon Dec 14 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.3-4
- Make it x86/x86_64 only.

* Fri Dec 4 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.3-2
- Update to Linux Tools 0.4 release.

* Tue Sep 1 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.3-1
- Update to Linux Tools 0.3 release.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 14 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.2-3
- Update to LinuxTools 0.2 release.

* Mon Mar 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.2-2
- Rebuild to not ship p2 context.xml.

* Mon Feb 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.2-1
- Update to 0.4.2.

* Tue Jan 6 2009 Alexander Kurtakov <akurtako@redhat.com> 0.4.1-1
- New version 0.4.1.
- Fix URL and fetch script to use tags.

* Sat Oct 11 2008 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.4.0-6
- Omit empty debuginfo pkg (Ville Skyttä #472651)

* Sat Oct 11 2008 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.4.0-5
- Fix specfile

* Thu Oct 7 2008 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.4.0-4
- Remove gcj compilation
- Add %%{install_loc}

* Fri Oct 03 2008 Alexander Kurtakov <akurtako@redhat.com> 0.4.0-3
- Rebuild for #465109.

* Wed Jul 30 2008 Andrew Overholt <overholt@redhat.com> 0.4.0-2
- Update for Eclipse SDK 3.4
- Remove noarch potential since CDT is arch-specific and we
  ExclusiveArch

* Wed Jun 29 2008 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.4.0-1
- bump to 0.4.0

* Wed Jun 25 2008 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.3.0-3
- Using pdebuild.

* Fri May 1 2008 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.3.0-2
- Bump to 0.3.0

* Wed Apr 23 2008 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.2.1-4
- Revert last changes

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.1-3
- Autorebuild for GCC 4.3

* Sat Dec 15 2007 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.2.1-2
- Add Sources completion (Contributed by Alexander Kurtakov)

* Sat Dec 15 2007 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.2.1-1
- RFE eclipse spec editor should allow users to configure the
  format of the changelog entry (#421881)

* Wed Nov 28 2007 fons <fons@xp2000.leafamily.org> 0.2.0-2
- Add support for URPM tool and cancel support to RpmPackageBuildProposalsJob.
- Fix Bug #207207

* Sun Oct 14 2007 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.1.0-10
- Just tag the sources correctly.

* Sun Oct 14 2007 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.1.0-9
- Fix https://bugs.eclipse.org/bugs/show_bug.cgi?id=206160
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=327101

* Mon Sep 24 2007 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.1.0-8
- Fix https://bugs.eclipse.org/bugs/show_bug.cgi?id=204146
- Fix https://bugs.eclipse.org/bugs/show_bug.cgi?id=204150

* Mon Sep 3 2007 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.1.0-7
- Requires rpmlint >= 0.81

* Mon Sep 3 2007 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.1.0-6
- Remove rpmlint-remove-rpmlint-plugin.patch because rpmlint 0.81 is out.

* Sun Sep 2 2007 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.1.0-5
- Only build the plugin where the changelog plugin can be build, only
  x86 x86_64 ppc and ia64 arches are supported by the changelog plugin because
  of dependencies on the cdt plugin.

* Sat Sep 1 2007 Alphonse Van Assche <alcapcom@fedoraproject.org> 0.1.0-4
- Disable temporarily rpmlint Plug-In because rpmlint 0.80 is not supported.

* Thu Aug 29 2007 Alphonse Van Assche <alcapcom@gmail.com> 0.1.0-3
- Fix the description tag (see comment 9 of #253434for more details).
- Lower the rpmlint required version form 0.81 to 0.80.

* Sun Aug 26 2007 Alphonse Van Assche <alcapcom@gmail.com> 0.1.0-2
- Fix License tag.

* Wed Aug 15 2007 Alphonse Van Assche <alcapcom@gmail.com> 0.1.0-1
- Initial package.
