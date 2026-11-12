pkgname = "mango"
pkgver = "0.18.5"
_commit = "26e37089e58bae5009e1ecce0b65e9214de186a9"  # wl-only branch
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dxwayland=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "cjson-devel",
    "pango-devel",
    "pcre2-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
]
depends = ["xwayland"]
pkgdesc = "Practical, Powerful, Pretty Wayland Compositor"
license = "GPL-3.0-only"
url = "https://mangowm.github.io"
source = f"https://github.com/mangowm/mango/archive/{_commit}.tar.gz"
sha256 = "94757f760b7225ffce2d3274e679623dd52d1c77c2cae5cca6c33637cc584f15"
options = ["etcfiles"]


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_license("LICENSE")
