pkgname = "museum"
pkgver = "1.7.24"
pkgrel = 0
build_wrksrc = "server"
build_style = "go"
make_build_args = ["./cmd/museum"]
hostmakedepends = ["cargo-auditable", "go", "pkgconf", "nodejs", "yarn"]
makedepends = ["dinit-chimera", "libsodium-devel"]
depends = ["postgresql"]
pkgdesc = "E2EE photo gallery"
license = "AGPL-3.0-only"
url = "https://ente.io"
source = f"https://github.com/ente-io/ente/archive/photosd-v{pkgver}.tar.gz"
sha256 = "aa3a80765ffd53b2febe476ebc68450e51e6089a012acb99bcfe9232a4c8b805"
broken_symlinks = ["usr/share/museum/museum.yaml"]

_apps = [
    "photos",
    "albums",
    "accounts",
    "auth",
    "cast",
    "share",
    "embed",
    "memories",
]


def prepare(self):
    from cbuild.util import cargo

    self.golang.mod_download(wrksrc=build_wrksrc)

    self.log("cargo: downloading dependencies")
    cargo.Cargo(self).vendor(wrksrc="rust")

    self.log("yarn: downloading dependencies")
    self.do(
        "yarn", "install", "--frozen-lockfile", allow_network=True, wrksrc="web"
    )


def pre_build(self):
    self.log("yarn: running build")

    self.env["NEXT_PUBLIC_ENTE_ENDPOINT"] = "http://localhost:8080"
    for app in _apps:
        self.do("yarn", "--offline", f"build:{app}", wrksrc="../web")


def post_install(self):
    for data in [
        "configurations",
        "migrations",
        "mail-templates",
        "web-templates",
    ]:
        self.install_files(data, "usr/share/museum")

    for app in _apps:
        self.install_files(
            f"../web/apps/{app}/out", f"usr/share/museum/apps/{app}"
        )

    self.install_link(
        "usr/share/museum/museum.yaml", "../../../etc/museum/museum.yaml"
    )
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "museum")
    self.install_license(self.srcdir / "LICENSE")
