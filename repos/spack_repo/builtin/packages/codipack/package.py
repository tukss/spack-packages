# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import generic
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Codipack(CMakePackage, Package):
    """CoDiPack is a C++-library that enables the computation of gradients in computer programs
    using Algorithmic Differentiation. It is based on the Operator Overloading approach and uses
    static polymorphism and expression templates, resulting in an extremely fast evaluation of
    adjoints or forward derivatives. It is specifically designed with HPC applications in mind."""

    homepage = "https://www.scicomp.uni-kl.de/software/codi/"
    url = "https://github.com/SciCompKL/CoDiPack/archive/refs/tags/v2.1.0.tar.gz"
    git = "https://github.com/SciCompKL/CoDiPack.git"

    version("3.0.0", sha256="cc25ae436118d1347f8efa7fd0df4c0af00b48e910133ecdbce97968084a9106")
    version("2.3.2", sha256="82efa259139b95ce1f1447e6f8180b139f61e7b361e9c1bcd36a78feaab099ca")
    version("2.3.1", sha256="c36821f31da9cc0c5b3e9e6c398cc18337db0117a023364781f9a2289aa69e28")
    version("2.3.0", sha256="43f976e23a6a77de7e858e474159026ebe93d480274ab389721b8cf78d9124cc")
    version("2.2.0", sha256="24e9129829588fd8965620f275e40ae3a0be3b24015bc7d7280fa5ad551c10ac")
    version("2.1.0", sha256="c8d07eb01eaa056175902d5b153b8606b05d208ff0a541d15284f4d9ff6e87c2")
    version("2.0.2", sha256="c6eecfdbf5818daf80871461f23f8a29b5b72e314d2034047d0b0fcd44744339")
    version("1.9.3", sha256="27dd92d0b5132de37b431989c0c3d5bd829821a6a2e31e0529137e427421f06e")
    version("openmp", branch="experimentalOpenMPSupport")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.12:", type="build", when="@2.1.0:")

    build_system(
        conditional("cmake", when="@2.1.0:"),
        conditional("generic", when="@:2.0.2"),
        default="cmake",
    )


class GenericBuilder(generic.GenericBuilder):
    def install(self, pkg, spec, prefix):
        mkdirp(join_path(prefix, "include"))
        install_tree(join_path(self.stage.source_path, "include"), join_path(prefix, "include"))
