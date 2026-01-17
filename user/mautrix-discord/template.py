pkgname = "mautrix-discord"
pkgver = "0.7.5"
pkgrel = 0
build_style = "go"
make_build_args = [
    # Can set other data asuch as BuildTime and Commit
    # but AFAIK there is no way to get that here in a template
    f"-ldflags=-X main.Tag={pkgver}",
]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera", "olm-devel"]
depends = ["postgresql"]
pkgdesc = "Matrix-Discord puppeting bridge"
license = "AGPL-3.0-only"
url = "https://go.mau.fi/mautrix-discord"
source = f"https://github.com/mautrix/discord/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "376b13f99d1cd15408eb580f5c09e0b85eab5d07c552db43fd45ab52cb31c83d"
# no tests
options = ["!check"]

def post_install(self):
    # Requires user to copy file and chmod as 646
    self.install_file("example-config.yaml", "usr/share/examples/mautrix-discord")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "mautrix-discord")
    self.install_license("LICENSE")
