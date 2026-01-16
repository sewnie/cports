pkgname = "tuwunel"
pkgver = "1.6.0"
pkgrel = 0
build_style = "cargo"
make_check_env = {"TUWUNEL_DATABASE_PATH": "/tmp/tuwunel-smoketest.db"}
hostmakedepends = ["cargo-auditable", "cmake", "pkgconf", "rust-rustfmt"]
makedepends = [
    "dinit-chimera",
    "liburing-devel",
    "linux-headers",
    "rust-std",
    "zstd-devel",
]
pkgdesc = "Community-driven Matrix homeserver"
license = "Apache-2.0"
url = "https://tuwunel.org"
source = f"https://github.com/matrix-construct/tuwunel/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "aab44526cb14244f139089c7ff5ea397cbe044896c7cddf1d74f76274bcfe6ba"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/tuwunel")
    self.install_file("tuwunel-example.toml", "usr/share/examples/tuwunel")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "tuwunel")
    self.install_license("LICENSE")
