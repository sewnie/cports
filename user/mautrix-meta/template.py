pkgname = "mautrix-meta"
pkgver = "0.2512.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    # Can set other data asuch as BuildTime and Commit
    # but AFAIK there is no way to get that here in a template
    f"-ldflags=-X main.Tag={pkgver}",
    "./cmd/mautrix-meta",
]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera", "olm-devel"]
depends = ["postgresql"]
pkgdesc = "Matrix-Facebook Messenger and Instagram DM puppeting bridge"
license = "AGPL-3.0-only"
url = "https://go.mau.fi/mautrix-meta"
source = f"https://github.com/mautrix/meta/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3d0021f1a42ab4886f1c7db85dcb5b52aca22d93409d2a33c9e6af161f74ea55"
# no tests
options = ["!check"]

def post_install(self):
    self.do(f"{self.make_dir}/mautrix-meta", "--generate-example-config")
    self.install_file("config.yaml", "etc/mautrix-meta", mode=646) # allow _mautrix-meta to update
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "mautrix-meta")
    self.install_license("LICENSE")
