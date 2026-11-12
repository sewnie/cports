pkgname = "libigloo"
pkgver = "0.9.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["rhash-devel"]
pkgdesc = "Generic C framework used by Icecast"
license = "GPL-2.0-or-later"
url = "https://icecast.org"
source = f"https://downloads.xiph.org/releases/igloo/libigloo-{pkgver}.tar.gz"
sha256 = "ea22e9119f7a2188810f99100c5155c6762d4595ae213b9ac29e69b4f0b87289"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libigloo-devel")
def _(self):
    return self.default_devel()
