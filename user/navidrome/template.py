pkgname = "navidrome"
pkgver = "0.64.2"
_commit = "ec2e0a9ea9cd7c2f08f930fc0579b991e1fe0900"
pkgrel = 0
build_style = "go"
make_env = {
    "CGO_ENABLED": "1",
    "ND_ENABLEINSIGHTSCOLLECTOR": "false",
}
make_build_args = [
    f"-ldflags= -X github.com/navidrome/navidrome/consts.gitTag={pkgver}"
]
hostmakedepends = ["go", "nodejs"]
makedepends = ["dinit-chimera", "sqlite-devel"]
checkdepends = ["zip"]
pkgdesc = "OpenSubsonic music server"
license = "GPL-3.0-or-later"
url = "https://www.navidrome.org"
source = f"https://github.com/navidrome/navidrome/archive/{_commit}.tar.gz"
sha256 = "8af67e5e5c7a8f3506b4872d04815ac834275ef4672aac7ec63d25fcc7c4a75d"
tool_flags = {"GOFLAGS": ["-tags=netgo,sqlite_fts5"]}
# cannot be bothered
options = ["!check"]


def prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()
    golang.Golang(self).mod_download(
        wrksrc="plugins/testdata/partial-metadata-agent"
    )

    self.log("npm: downloading dependencies")
    self.do("npm", "ci", allow_network=True, wrksrc="ui")


def pre_build(self):
    self.log("npm: running build")
    self.do("npm", "run", "build", wrksrc="ui")


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "navidrome")
    self.install_license("LICENSE")
