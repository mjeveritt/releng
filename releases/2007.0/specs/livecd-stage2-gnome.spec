subarch: alpha
version_stamp: 2007.0
target: livecd-stage2
rel_type: default
profile: default-linux/alpha/2007.0/desktop
snapshot: 2007.0
source_subpath: default/livecd-stage1-alpha-installer-2007.0

livecd/fstype: squashfs
livecd/cdtar: /usr/lib/catalyst/livecd/cdtar/aboot-0.9-r1-cdtar.tar.bz2

livecd/iso: /var/tmp/catalyst/builds/default/livecd-alpha-installer-2007.0.iso
#livecd/splash_type: gensplash
#livecd/splash_theme: livecd-2007.0
livecd/xdm: gdm
livecd/xsession: gnome
livecd/fsscript: /root/livecd/scripts/2007.0/livecd.sh

livecd/volid: Gentoo Linux alpha LiveCD 2007.0
livecd/users: gentoo
livecd/type: gentoo-release-livecd

livecd/overlay: /root/livecd/overlays/livecd/2007.0/common/overlay/livecd
livecd/root_overlay: /root/livecd/overlays/2007.0/common/root_overlay

livecd/bootargs: dokeymap
livecd/gk_mainargs: --lvm2 --dmraid --evms2

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /root/livecd/kconfig/releases/2007.0/alpha/livecd-2.6.19.config
boot/kernel/gentoo/use: usb oss atm
boot/kernel/gentoo/packages:
	media-libs/alsa-lib
	media-libs/alsa-oss
	media-sound/alsa-utils
	sys-fs/cryptsetup-luks

livecd/empty:
	/var/tmp
	/var/empty
	/var/run
	/var/state
	/var/cache/edb/dep
	/tmp
	/usr/portage
	/usr/src
	/root/.ccache
	/etc/splash/gentoo
	/etc/splash/emergence
	/usr/share/genkernel/pkg/amd64/cpio

livecd/rm:
	/etc/*-
	/etc/*.old
	/root/.viminfo
	/var/log/*.log
	/usr/share/genkernel/pkg/amd64/*.bz2
