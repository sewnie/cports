pkgname = "cambalache"
pkgver = "1.6.0"
_commit = "de3ffefbb1d42c605c623854a3c2520dc2874339"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "libadwaita-devel",
    "libx11-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "meson",
    "pkgconf",
    "python-lxml",
    "wlroots0.20-devel",
]
makedepends = [
    "gtksourceview-devel",
    "libhandy-devel",
    "python-gobject-devel",
    "wayland-protocols",
]
depends = [
    "gsettings-desktop-schemas",
    "gtksourceview",
    "python-gobject",
    "python-lxml",
    "webkitgtk4",
]
checkdepends = ["python-pytest"]
pkgdesc = "New RAD tool for Gtk 4 and 3"
license = "LGPL-2.1-only"
url = "https://gitlab.gnome.org/jpu/cambalache"
source = [
    f"{url}/-/archive/{_commit}/cambalache-{_commit}.tar.gz",
    "https://gitlab.gnome.org/jpu/casilda/-/archive/1.6.0/casilda-1.6.0.tar.gz",
]
source_paths = [".", "subprojects/casilda"]
sha256 = [
    "e3651431ee0f39f982817572e680d41bc4281dace3ab1c62bbfb2b128ce01457",
    "2dcc9b8b73f92ac6149a991d458dd22a5384bb0396d20af6feda6b66a39f9096",
]
# until GObject is fixed
options = ["!check"]
