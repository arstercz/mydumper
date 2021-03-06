# norootforbuild

Name:		mydumper
Version:	0.9.5
Release:	3%{?dist}
Summary:	How MySQL DBA & support engineer would imagine 'mysqldump'
Source:		%{name}-%{version}.tar.gz
URL:		https://github.com/maxbube/mydumper
Group:		Applications/Databases
License:	GNU General Public License version 3 (GPL v3)
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: glibc-devel
# Change for RHEL
#BuildRequires: libmysqlclient-devel
BuildRequires: mysql-devel
BuildRequires: make
BuildRequires: pcre-devel
BuildRequires: zlib-devel
BuildRequires: cmake
# Change for RHEL 5
BuildRoot: %{_tmppath}/%{name}-root

%description
mydumper is complement to mysqldump, for MySQL data dumping, providing:

1. Parallelism (hence, speed) and performance (avoids expensive character set
   conversion routines, efficient code overall)
2. Easier to manage output (separate files for tables, dump metadata, etc, easy
   to view/parse data)
3. Consistency - maintains snapshot across all threads, provides accurate
   master and slave log positions, etc
4. Manageability - supports PCRE for specifying database and tables inclusions
   and exclusions

It does not support schema dumping and leaves that to 'mysqldump --no-data'

It was born as weekend experiment, and apparently it worked well enough to have
public appearance.

Authors:
--------
	Andrew Hutchins <andrew.hutchins@sun.com>
	Domas Mituzas <domas@dammit.lt>
	Mark Leith <mark.leith@sun.com>

%prep
%setup

echo buildroot: %{buildroot}

%build
cmake -DCMAKE_INSTALL_PREFIX="%{_prefix}" . -DMYSQL_LIBRARIES_mysqlclient:FILEPATH=/usr/lib64/mysql/libmysqlclient.a
%__make OPTFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%__mkdir -p %{buildroot}/%{_bindir}
#%__install -m 755 %{name} %{buildroot}/%{_bindir}
# Update installation procedure manually
%__install -m 755 mydumper %{buildroot}/%{_bindir}
%__install -m 755 myloader %{buildroot}/%{_bindir}

%clean
%__rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
#%{_bindir}/%{name}
%{_bindir}/mydumper
%{_bindir}/myloader

%changelog

* Thu Jul 09 2020 chenzhe07@gmail.com - 0.9.5-3
- Update to 0.9.5-3
- merge the latest commits;
- ignore extra space in procedure, function, events...

* Sat May 05 2018 nkadel@skyhook.com - 0.9.5-2
- Update to 0.9.5


* Mon Sep 11 2017 nkadel@skyhook.com - 0.9.3-0.1
- Update to 0.9.3

* Tue Dec 06 2016 nkadel@skyhook.com - 0.9.1-0.4
- Add specific deployment of mydumper and myloader

* Fri Oct 14 2016 nkadel@skyhook.com - 0.9.1-0.3
- Switch to "buildroot" for RHEL 5 compilation

* Mon Aug 15 2016 nkadel@skyhook.com - 0.9.1-0.2
- Correct Source URL

* Sat Apr 30 2016 nkadel@skyhookwireless.com - 0.9.1-0.1
- Update to 0.9.1
- Adapt for RHEL compilation
* Sat May 30 2015 lenz@grimmer.com
- Update to 0.6.2
* Thu Mar 18 2010 lenz@grimmer.com
- Initial Package for the openSUSE Build Service (Version 0.1.7)
