# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack_repo.builtin.build_systems.generic import Package


class Krona(Package):
    """Krona Tools is a set of scripts to create Krona charts from several Bioinformatics tools as well as from text and XML files."""

    homepage = "https://github.com/marbl/Krona/wiki/KronaTools"
    url = "https://github.com/marbl/Krona/archive/refs/tags/v2.8.1.tar.gz"

    version(
        "2.8.1",
        sha256="d57eb342427c179bc0431b8a6088313f54326e233762b5652e8a90ce3ca4027d",
    )

    depends_on("perl")

    def install(self, spec, prefix):
        mkdirp(prefix.dest)
        mkdirp(prefix.taxonomy)
        install_tree("KronaTools", prefix.dest)
        perl = which("perl")
        bash = which("bash")
        with working_dir(prefix.dest):
            perl("install.pl", "--prefix", prefix, "--taxonomy", prefix.taxonomy)
            bash("updateTaxonomy.sh")
            # bash('updateAccessions.sh')
