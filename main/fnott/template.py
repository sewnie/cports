pkgname = "fnott"
_commit = "e71bbfedbeffa4f5c5bdec8e286e87385274d074"
pkgver = "1.8.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
    "wayland-devel",
]
makedepends = [
    "dbus-devel",
    "dinit-chimera",
    "dinit-dbus",
    "fcft-devel",
    "linux-headers",
    "pixman-devel",
    "tllist",
    "turnstile",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["dinit-dbus"]
pkgdesc = "Keyboard driven wayland notification daemon"
license = "MIT"
url = "https://codeberg.org/dnkl/fnott"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "b2e6d13f8d007734ddab1d688013497abb74899cb62e194f11f5d2733131a12f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "fnott.user")
