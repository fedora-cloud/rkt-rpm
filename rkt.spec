%if 0%{?fedora} || 0%{?rhel} == 6
%global with_devel 0
%global with_bundled 1
%global with_debug 0
%global with_check 1
%global with_unit_test 0
%else
%global with_devel 0
%global with_bundled 1
%global with_debug 0
%global with_check 0
%global with_unit_test 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider github
%global provider_tld com
%global project coreos
%global repo rkt

%global git0 https://%{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
%global commit0 3386b89af6bf3df0af5a74110ac1bc0719f011c8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# valid values: coreos usr-from-src usr-from-host
%global stage1_flavors host

Name: %{repo}
Version: 1.6.0
Release: 3.git%{shortcommit0}%{?dist}
Summary: CLI for running app containers
License: ASL 2.0
URL: https://%{import_path}
ExclusiveArch: x86_64
Source0: %{git0}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bc
BuildRequires: glibc-static
BuildRequires: golang >= 1.6
BuildRequires: gperf
BuildRequires: gnupg
BuildRequires: intltool
BuildRequires: libacl-devel
BuildRequires: libcap-devel
BuildRequires: libgcrypt-devel
BuildRequires: libtool
BuildRequires: libmount-devel
BuildRequires: libxkbcommon-devel
BuildRequires: trousers-devel
BuildRequires: perl-Config-Tiny
BuildRequires: squashfs-tools
BuildRequires: systemd >= 222

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(camlistore.org/pkg/legal)
BuildRequires: golang(github.com/coreos/etcd/client)
BuildRequires: golang(github.com/appc/cni/pkg/invoke)
BuildRequires: golang(github.com/appc/cni/pkg/ip)
BuildRequires: golang(github.com/appc/cni/pkg/ns)
BuildRequires: golang(github.com/appc/cni/pkg/types)
BuildRequires: golang(github.com/appc/docker2aci/lib/backend/file)
BuildRequires: golang(github.com/appc/docker2aci/lib/backend/repository)
BuildRequires: golang(github.com/appc/docker2aci/lib/common)
BuildRequires: golang(github.com/appc/docker2aci/lib/types)
BuildRequires: golang(github.com/appc/docker2aci/lib/util)
BuildRequires: golang(github.com/appc/docker2aci/tarball)
BuildRequires: golang(github.com/appc/spec/aci)
BuildRequires: golang(github.com/appc/spec/pkg/acirenderer)
BuildRequires: golang(github.com/appc/spec/pkg/device)
BuildRequires: golang(github.com/appc/spec/pkg/tarheader)
BuildRequires: golang(github.com/appc/spec/schema)
BuildRequires: golang(github.com/appc/spec/schema/common)
BuildRequires: golang(github.com/appc/spec/schema/types)
BuildRequires: golang(github.com/bradfitz/http2)
BuildRequires: golang(github.com/bradfitz/http2/hpack)
BuildRequires: golang(github.com/camlistore/camlistore/pkg/errorutil)
BuildRequires: golang(github.com/camlistore/lock)
BuildRequires: golang(github.com/coreos/go-iptables/iptables)
BuildRequires: golang(github.com/coreos/go-semver/semver)
BuildRequires: golang(github.com/coreos/go-tspi/attestation)
BuildRequires: golang(github.com/coreos/go-tspi/tspi)
BuildRequires: golang(github.com/coreos/ioprogress)
BuildRequires: golang(github.com/cpuguy83/go-md2man/md2man)
BuildRequires: golang(github.com/cznic/b)
BuildRequires: golang(github.com/cznic/bufs)
BuildRequires: golang(github.com/cznic/exp/lldb)
BuildRequires: golang(github.com/cznic/fileutil)
BuildRequires: golang(github.com/cznic/fileutil/falloc)
BuildRequires: golang(github.com/cznic/fileutil/storage)
BuildRequires: golang(github.com/cznic/mathutil)
BuildRequires: golang(github.com/cznic/ql)
BuildRequires: golang(github.com/cznic/sortutil)
BuildRequires: golang(github.com/cznic/strutil)
BuildRequires: golang(github.com/cznic/zappy)
BuildRequires: golang(github.com/d2g/dhcp4)
BuildRequires: golang(github.com/godbus/dbus)
BuildRequires: golang(github.com/godbus/dbus/introspect)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/proto/testdata)
BuildRequires: golang(github.com/gorilla/context)
BuildRequires: golang(github.com/inconshreveable/mousetrap)
BuildRequires: golang(github.com/kballard/go-shellquote)
BuildRequires: golang(github.com/kr/pty)
BuildRequires: golang(github.com/petar/GoLLRB/llrb)
BuildRequires: golang(github.com/russross/blackfriday)
BuildRequires: golang(github.com/shurcooL/sanitized_anchor_name)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(github.com/vishvananda/netlink)
BuildRequires: golang(github.com/vishvananda/netlink/nl)
BuildRequires: golang(golang.org/x/crypto/cast5)
BuildRequires: golang(golang.org/x/crypto/openpgp/armor)
BuildRequires: golang(golang.org/x/crypto/openpgp/elgamal)
BuildRequires: golang(golang.org/x/crypto/openpgp/errors)
BuildRequires: golang(golang.org/x/crypto/openpgp/packet)
BuildRequires: golang(golang.org/x/crypto/openpgp/s2k)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/html/atom)
BuildRequires: golang(golang.org/x/net/internal/timeseries)
BuildRequires: golang(golang.org/x/net/trace)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(golang.org/x/tools/go/vcs)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/benchmark/grpc_testing)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/grpclog)
BuildRequires: golang(google.golang.org/grpc/health/grpc_health_v1alpha)
BuildRequires: golang(google.golang.org/grpc/metadata)
BuildRequires: golang(google.golang.org/grpc/naming)
BuildRequires: golang(google.golang.org/grpc/transport)
BuildRequires: golang(k8s.io/kubernetes/pkg/api/resource)
BuildRequires: golang(speter.net/go/exp/math/dec/inf)
BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/remyoudompheng/bigfft)
BuildRequires: golang(github.com/spf13/viper)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/oauth2/jwt)
BuildRequires: golang(golang.org/x/text/encoding)
BuildRequires: golang(golang.org/x/text/encoding/charmap)
BuildRequires: golang(golang.org/x/text/encoding/japanese)
BuildRequires: golang(golang.org/x/text/encoding/korean)
BuildRequires: golang(golang.org/x/text/encoding/simplifiedchinese)
BuildRequires: golang(golang.org/x/text/encoding/traditionalchinese)
BuildRequires: golang(golang.org/x/text/encoding/unicode)
BuildRequires: golang(golang.org/x/text/transform)
%endif

Requires(pre): shadow-utils
Requires(post): systemd >= 222
Requires(preun): systemd >= 222
Requires(postun): systemd >= 222

%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary: %{summary}
BuildArch: noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
%endif

%description devel
%{summary}

This package contains library source intended for building other packages
which use import path with %{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary: Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires: %{name}-devel = %{version}-%{release}

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{name}-%{commit0}

%build
./autogen.sh
# ./configure flags: https://github.com/coreos/rkt/blob/master/Documentation/build-configure.md
./configure --with-stage1-flavors=%{stage1_flavors} \
            --with-stage1-flavors-version-override=%{version}-%{release} \
            --with-stage1-default-location=%{_libexecdir}/%{name}/stage1-host.aci
GOPATH=$GOPATH:%{gopath}:$(pwd)/Godeps/_workspace make all bash-completion

%install
# install binaries
install -dp %{buildroot}{%{_bindir},%{_libexecdir}/%{name},%{_unitdir}}
install -dp %{buildroot}%{_sharedstatedir}/%{name}

install -p -m 755 build-%{name}-%{version}+git/bin/%{name} %{buildroot}%{_bindir}
install -p -m 755 dist/scripts/setup-data-dir.sh %{buildroot}%{_bindir}/%{name}-setup-data-dir.sh
install -p -m 644 build-%{name}-%{version}+git/bin/stage1-host.aci %{buildroot}%{_libexecdir}/%{name}

# install bash completion
install -dp %{buildroot}%{_datadir}/bash-completion/completions
install -p -m 644 dist/bash_completion/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}

# install metadata unitfiles
install -p -m 644 dist/init/systemd/%{name}-gc.timer %{buildroot}%{_unitdir}
install -p -m 644 dist/init/systemd/%{name}-gc.service %{buildroot}%{_unitdir}
install -p -m 644 dist/init/systemd/%{name}-metadata.socket %{buildroot}%{_unitdir}
install -p -m 644 dist/init/systemd/%{name}-metadata.service %{buildroot}%{_unitdir}

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
export GOPATH=%{buildroot}/%{gopath}:$(pwd)/Godeps/_workspace:%{gopath}
%endif
%endif

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
exit 0

%post
%{_bindir}/%{name}-setup-data-dir.sh
%systemd_post %{name}-metadata.service

%preun
%systemd_preun %{name}-metadata.service

%postun
%systemd_postun_with_restart %{name}-metadata.service

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTING.md DCO README.md Documentation/*
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc CONTRIBUTING.md DCO README.md Documentation/*
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md DCO README.md Documentation/*
%{_bindir}/%{name}
%{_bindir}/%{name}-setup-data-dir.sh
%{_libexecdir}/%{name}/stage1-host.aci
%{_unitdir}/%{name}*
%{_datadir}/bash-completion/completions/%{name}
%{_sharedstatedir}/%{name}

%changelog
* Sat May 21 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.6.0-3.git3386b89
- built commit 3386b89

* Thu May 19 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.6.0-2.gitde05a39
- built commit#de05a39

* Sat May 14 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.6.0-1.git7740f9d
- Resolves: #1336072 - bump to v1.6.0
- built commit 7740f9d

* Fri May 06 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.5.1-1.git38b4462
- Resolves: #1327805 - bump to v1.5.1
- built commit 38b4462

* Sat Apr 02 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.3.0-1.gitb6a73a7
- Resolves: rhbz#1323388 - bump to v1.3.0
- built commit#b6a73a7

* Wed Mar 30 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2.1-2.gitadc2bbd
- built commit#adc2bbd

* Fri Mar 25 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.2.1-1.gite568957
- built commit#e568957

* Fri Mar 18 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-10.gitff0813b
- built commit#ff0813b

* Mon Mar 14 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-9.git990029c
- built commit#990029c

* Fri Mar 11 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-8.git0aacba3
- built commit#0aacba3

* Wed Mar 09 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-7.git7b07bf2
- built commit#7b07bf2

* Mon Mar 07 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-6.gite2c3011
- built commit#e2c3011

* Sun Mar 06 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-5.git63522c3
- built commit#63522c3

* Fri Mar 04 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-4.git63522c3
- built commit#63522c3

* Wed Mar 02 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-3.git5a19dc6
- built commit#5a19dc6

* Wed Mar 02 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-2.git5a19dc6
- built commit#5a19dc6

* Fri Feb 26 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.1.0-1.gitdebc46e
- built commit#debc46e

* Thu Feb 25 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-13.gitd4db664
- built commit#d4db664

* Wed Feb 24 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-12.git07235a7
- built commit#07235a7

* Tue Feb 23 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-11.git9003f4a
- do not remove /var/lib/rkt on uninstall

* Tue Feb 23 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-10.git9003f4a
- built commit#9003f4a

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9.gitd842d09
- https://fedoraproject.org/wiki/Changes/golang1.6

* Mon Feb 22 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-8.gitd842d09
- built commit#d842d09

* Thu Feb 18 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-7.gitd2b211d
- built commit#d2b211d

* Thu Feb 18 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-6.gitd2b211d
- built commit#d2b211d

* Sun Feb 14 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-5.gitf529cc2
- built commit#f529cc2

* Fri Feb 05 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-4.git6ce1d5f
- built commit#6ce1d5f

* Thu Feb 04 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-3.git6146a78
- built commit#6146a78

* Thu Feb 04 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-2.git6146a78
- built commit#6146a78

* Thu Feb 04 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-1.git6146a78
- built commit#6146a78

* Wed Feb 03 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.16.0-6.git5a8ee7d
- built commit#5a8ee7d

* Mon Feb 01 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.16.0-5.gite542f81
- built commit#e542f81

* Wed Jan 27 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.16.0-4.git646746d
- built commit#646746d

* Mon Jan 25 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.16.0-3.git6ad1d4a
- built commit#6ad1d4a

* Sun Jan 24 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.16.0-2.gitf37aae6
- built commit#f37aae6

* Fri Jan 22 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.16.0-1.git43e4d22
- Resolves: rhbz#1300874 - bump to v0.16.0
- built commit#43e4d22

* Thu Jan 14 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.15.0-4.git5988b72
- install bash completion

* Thu Jan 14 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.15.0-3.git5988b72
- built commit#5988b72
- Alban Crequy <alban.crequy@gmail.com> provided fixes for configure flags
and dir paths installed

* Sun Jan 10 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.15.0-2.git7575500
- built commit#7575500

* Mon Aug 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.7.0-3.git6dae5d5
- built rkt commit#6dae5d5

* Mon Aug 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.7.0-2.git6dae5d5
- built rkt commit#6dae5d5

* Sun Jul 19 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.7.0-1
- New version: 0.7.0, built rkt         commit#c5e8cd5

* Wed Jun 17 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.6.1-1
- New version: 0.6.1, built rkt         commit#30cb88c

* Wed Jun 10 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.6-5.git06bf23b
- built rkt commit#06bf23b

* Sun Jun 07 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.6-4.git7bf926e
- built rkt commit#7bf926e

* Tue Jun 02 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.6-3.git25b862d
- built rkt commit#25b862d

* Fri May 29 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.6-2.gited97885
- built rkt commit#ed97885

* Thu May 28 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.6-1
- New version: 0.5.6, built rkt         commit#139af2b

* Wed May 27 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-7.git5e95eac
- built rkt commit#5e95eac

* Sun May 24 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-6.gite5be761
- built rkt commit#e5be761

* Mon May 11 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-5.git724e49e
- built rkt commit#724e49e

* Mon May 11 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-4.git724e49e
- built rkt commit#724e49e

* Fri May 08 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-3.gitd61a4c5
- built rkt commit#d61a4c5

* Mon May 04 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-2.gitb1190d9
- built rkt commit#b1190d9

* Mon May 04 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.5-1
- New version: 0.5.5, built rkt         commit#b1190d9

* Wed Apr 29 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.4-3.git40ecb47
- built rkt commit#40ecb47

* Wed Apr 29 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.4-2.git%{d_shortcommit}
- built rkt commit#40ecb47

* Thu Apr 23 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-16.gita506a39
- built rkt commit#a506a39

* Tue Apr 21 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-15.git73e6e1e
- built rkt commit#73e6e1e

* Mon Apr 13 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-14.git7bcbe3f
- built rkt commit#7bcbe3f

* Sun Apr 12 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-13.git7bcbe3f
- built rkt commit#7bcbe3f

* Wed Apr 08 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-12.git96d0cc0
- built rkt commit#96d0cc0

* Tue Apr 07 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-11.gitfd44be4
- built rkt commit#fd44be4

* Sun Apr 05 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-10.gitb9bfa72
- built rkt commit#b9bfa72

* Sat Apr 04 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-9.gitb9bfa72
- built rkt commit#b9bfa72

* Fri Apr 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-8.gitae78000
- built rkt commit#ae78000

* Fri Apr 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-7.gitae78000
- built rkt commit#ae78000

* Fri Apr 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-6.gitae78000
- built rkt commit#ae78000

* Fri Apr 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-5.gitae78000
- built rkt commit#ae78000

* Fri Apr 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-4.gitae78000
- built rkt commit#ae78000

* Fri Apr 03 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-3.gitae78000
- built rkt commit#ae78000

* Thu Apr 02 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-2.gita72ad99
- install stage1.aci and metadata socket file

* Thu Apr 02 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.3-1.gita72ad99
- update to 0.5.3+git

* Sat Mar 28 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.1-2.git9d66f8c
- use github.com/lsm5/rkt branch systemd-vendored which includes a checked
out systemd v215 tree instead of git cloning it
- should allow building the rpm in a mock/koji environment

* Fri Mar 27 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.1-1.git58bd354
- update to latest upstream master

* Mon Feb 02 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.2.0-1.git29d53af
- use latest master commit
- mkrootfs uses fedora docker base image from koji
via Václav Pavlin <vpavlin@redhat.com>

* Tue Dec 02 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1.0-1.git553023e
- Initial package
- install init in libexec/rkt/stage1
https://github.com/coreos/rkt/issues/173
thanks Jonathan Boulle <jonathan.boulle@coreos.com>
and Tom Prince <tom.prince@ualberta.net>
