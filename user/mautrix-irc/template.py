pkgname = "mautrix-irc"
pkgver = "0_git20260418"
_commit = "edfa0857dce82651d210476474b548b9a76a0c6e"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/mautrix-irc"]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera", "olm-devel"]
depends = ["postgresql"]
pkgdesc = "Matrix-IRC puppeting bridge"
license = "AGPL-3.0-only"
url = "https://go.mau.fi/mautrix-irc"
source = f"https://github.com/mautrix/irc/archive/{_commit}.tar.gz"
sha256 = "55ebeef6166343144bb01fae57e5c69bb1404f538f526594126855e81a9a1203"
# no tests
options = ["!check"]


def post_install(self):
    # TODO: generate with -e
    self.install_file(
        "pkg/connector/example-config.yaml",
        "etc/mautrix-irc",
        name="config.yaml",
    )
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "mautrix-irc")
    self.install_license("LICENSE")
