Name:           chtc-release
Version:        1
Release:        1%{?dist}
Summary:        CHTC repository configuration

License:        ASL 2.0
URL:            https://github.com/CHTC/packaging

BuildRequires:  sed

BuildArch:      noarch
Requires:       redhat-release >= %{rhel}
Source0:        chtc-development.repo.in
Source1:        chtc-testing.repo.in
Source2:        chtc.repo.in

Source41:       RPM-GPG-KEY-CHTC

Requires:       redhat-release >= %{rhel}


%description
This package contains the CHTC repository configuration for YUM.

%prep
exit 0

%build
# generate .repo files for current rhel version
for infile in "%{SOURCE0}" "%{SOURCE1}" "%{SOURCE2}"; do
  outfile=$(basename "$infile" .in)
  sed "s/<RHEL>/%{rhel}/g" "$infile" > "$outfile"
done


%install

#GPG Key
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg
install -pm 644 %{SOURCE41} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-CHTC

# yum
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

install -m 644 *.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/RPM-GPG-KEY-CHTC


%changelog
* Mon Feb 26 2024 Mátyás Selmeci <matyas@cs.wisc.edu> - 1-1
- Created
