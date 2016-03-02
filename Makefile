DIST?=.el7.centos
#MOCK=planex-cache --cachedirs=/rpmcache
FETCH_EXTRA_FLAGS=--mirror file:///distfiles/ocaml2
MOCK_FLAGS ?= --configdir=$(TOPDIR)/mock \
              --resultdir=$(dir $@) --uniqueext=$(notdir $@) \
              --disable-plugin=package_state


include /usr/share/planex/Makefile.rules

_build/SOURCES/sysconfig_kernel-xen: ../xen-4.6/mk/sysconfig_kernel-xen
	cp $< $@

_build/SOURCES/xl.conf: ../xen-4.6/mk/xl.conf
	cp $< $@

_build/SOURCES/logrotate-xen-tools: ../xen-4.6/mk/logrotate-xen-tools
	cp $< $@

_build/SOURCES/ipxe.tar.gz: SPECS/xen.spec
	tar zcvf $@ ../ipxe

_build/SOURCES/macros.kernel: ../linux-3.x/mk/macros.kernel
	cp $< $@
