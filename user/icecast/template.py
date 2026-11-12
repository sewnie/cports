pkgname = "icecast"
pkgver = "2.5.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = [
    "curl-devel",
    "dinit-chimera",
    "libigloo-devel",
    "libvorbis-devel",
    "libxml2-devel",
    "libxslt-devel",
    "openssl3-devel",
    "rhash-devel",
]
checkdepends = ["bash"]
pkgdesc = "Streaming media server for Ogg/MP3/AAC streams"
license = "GPL-2.0-or-later"
url = "https://icecast.org"
source = (
    f"https://downloads.xiph.org/releases/icecast/{pkgname}-{pkgver}.tar.gz"
)
sha256 = "d9aa07c7429aec19d950ff6fd425c371f77158cd34ff220fc191b2c186c67c7a"
# tests require port access
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "icecast")
