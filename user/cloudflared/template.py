pkgname = "cloudflared"
pkgver = "2026.3.0"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags= -X main.Version={pkgver}",
    "./cmd/cloudflared",
]
make_install_args = [*make_build_args]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "Cloudflare Tunnel client"
license = "Apache-2.0"
url = "https://github.com/cloudflare/cloudflared"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "1c9e88653f091d3085975e50c2cf7308923c88ed5c82afe7fb98938d3f9c93ad"
# tests require ICMP proxy ports
options = ["!check"]


def post_build(self):
    self.do("make", f"VERSION={pkgver}", "cloudflared.1")


def post_install(self):
    self.install_man("cloudflared.1")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "cloudflared")
    self.install_license("LICENSE")
