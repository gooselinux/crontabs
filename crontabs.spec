Summary: Root crontab files used to schedule the execution of programs
Name: crontabs
Version: 1.10
Release: 32.1%{?dist}
License: Public Domain and GPLv2
Group: System Environment/Base
# no URL - it's only a one script which is used by different packages
Source0: crontab
Source1: run-parts
Source2: crontabs.4
BuildArch: noarch
Requires: /etc/cron.d
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The crontabs package contains root crontab files and directories.
You will need to install cron daemon to run the jobs from the crontabs.
The cron daemon such as cronie or fcron checks the crontab files to
see when particular commands are scheduled to be executed.  If commands
are scheduled, it executes them.

Crontabs handles a basic system function, so it should be installed on
your system.

%prep
#empty
%build
#empty

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/cron.{hourly,daily,weekly,monthly}
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man4/
install -m644 %SOURCE0 $RPM_BUILD_ROOT/etc/crontab
install -m755 %SOURCE1 $RPM_BUILD_ROOT/usr/bin/run-parts
install -m644 %SOURCE2 $RPM_BUILD_ROOT/%{_mandir}/man4/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/run-parts
%config(noreplace) /etc/crontab
%{_mandir}/man4/*
%dir /etc/cron.hourly
%dir /etc/cron.daily
%dir /etc/cron.weekly
%dir /etc/cron.monthly

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.10-32.1
- Rebuilt for RHEL 6

* Mon Oct 12 2009 Marcela Mašláňová <mmaslano@redhat.com> 1.10-32
- rebuilt for review

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Marcela Mašláňová <mmaslano@redhat.com> 1.10-30
- 491793 thanks Andrew Hecox for patch which allows set allow/deny jobs
- comment change "empty crontab"

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Marcela Mašláňová <mmaslano@redhat.com> 1.10-28
- 474219 requires on /etc/cron.d

* Mon Jan 26 2009 Marcela Mašláňová <mmaslano@redhat.com> 1.10-27
- Change requires back to cronie.

* Mon Jan 26 2009 Marcela Mašláňová <mmaslano@redhat.com> 1.10-26
- change /etc/crontab. All anacron jobs in cron.daily,weekly,...
 are check by anacron every hour. Anacron run them if they didn't
 run today. 

* Mon Dec  1 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> 1.10-25
- Added /etc/cron.{hourly,daily,weekly,monthly} dirs again. bz#473353

* Mon Jun  9 2008 Marcela Maslanova <mmaslano@redhat.com> 1.10-23
- 450084 LANG=C is set up for running scripts

* Wed May 28 2008 Marcela Maslanova <mmaslano@redhat.com> 1.10-22
- remove scripts for delay, anacron now own most of the scripts. 
Crontabs owns only run-parts, /etc/crontab and crontabs sysconfig.

* Mon May 5 2008 Marcela Maslanova <mmaslano@redhat.com> 1.10-21
- 445079 delay script failed in case DELAY is zero

* Fri Apr 4 2008 Marcela Maslanova <mmaslano@redhat.com> 1.10-20
- 440410 log pid of process instead of logger's pid

* Mon Oct 22 2007 Marcela Maslanova <mmaslano@redhat.com> 1.10-19
- run-parts log also end of each job (patch from J. Kamens)
- Resolves: rhbz#303081

* Tue Sep 25 2007 Marcela Maslanova <mmaslano@redhat.com> 1.10-18
- cron.{hourly, daily,...} run ok
- rhbz#296741

* Thu Aug 30 2007 Marcela Maslanova <mmaslano@redhat.com> 1.10-17
- better solution of configuration script

* Mon Aug 27 2007 Marcela Maslanova <mmaslano@redhat.com> 1.10-16
- 254220 typo in script run-parts

* Tue Aug 21 2007 Marcela Maslanova <mmaslano@redhat.com> 1.10-15
- corrected license tag in spec
- add config file to crontab - delay of cron.{daily,...} could be
    switch off
- Resolves: rhbz#253536

* Tue Feb 27 2007 Marcela Maslanova <mmaslano@redhat.com> 1.10-14
- review again

* Thu Feb  8 2007 Marcela Maslanova <mmaslano@redhat.com> 1.10-13
- rhbz#225662 review

* Mon Jan 29 2007 Marcela Maslanova <mmaslano@redhat.com> 1.10-12
- link daily,weekly,monthly
- rhbz#224687

* Wed Jan 24 2007 Marcela Maslanova <mmaslano@redhat.com> 1.10-11
- crontabs should ignore Cfengine files, rebuilt
- Resolves: rhbz#223472

* Wed Oct 11 2006 Marcela Maslanova <mmaslano@redhat.com> 1.10-9
- patch (#110894) for delaying more emails in the moment

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> 0 1.10-8
- rebuilt

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Sep 20 2004 Jason Vas Dias <jvdias@redhat.com>
- rebuilt under new CVS for dist-fc3

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb  7 2003 Bill Nottingham <notting@redhat.com>
- not-as-automated rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jul 19 2001 Preston Brown <pbrown@redhat.com>
- don't require tmpwatch

* Tue Feb 27 2001 Preston Brown <pbrown@redhat.com>
- noreplace crontab file; use tmppath

* Wed Jan 31 2001 Bill Nottingham <notting@redhat.com>
- don't process ,v files (#15968)

* Mon Aug  7 2000 Bill Nottingham <notting@redhat.com>
- put name of script in output of stuff run by run-parts (#12411)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun  6 2000 Bill Nottingham <notting@redhat.com>
- rebuild

* Fri Aug 27 1999 Jeff Johnson <jbj@redhat.com>
- don't run *~ or *, files (#4740).

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- don't run .rpm{save,new,orig} files (bug #2190)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Mon Nov 30 1998 Bill Nottingham <notting@redhat.com>
- crontab: set HOME=/

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- run-parts: skip sub-directories (e.g. CVS) found instead of complaining

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 07 1998 Erik Troan <ewt@redhat.com>
- moved crontab jobs up a bit to make sure they aren't confused by
  switching to and fro daylight savings time
  
* Fri Oct 24 1997 Erik Troan <ewt@redhat.com>
- removed tmpwatch and at entries

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
