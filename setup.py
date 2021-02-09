import setuptools
from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext
from distutils import sysconfig
import os

with open("README.md", "r") as fh:
    long_description = fh.read()


class NoSuffixBuilder(build_ext):
    def get_ext_filename(self, ext_name):
        filename = super().get_ext_filename(ext_name)
        suffix = sysconfig.get_config_var('EXT_SUFFIX')
        return filename.replace(suffix, "")


extensions = [Extension("pycpp_lib/mylib_core",
                        ["pycpp_lib/cpp/lib.cpp"],
                        depends=["pycpp_lib/cpp/lib.h"],
                        include_dirs=["pycpp_lib/cpp"],),]

setuptools.setup(
    name="libcppython", # Replace with your own username
    version="0.0.7",
    author="Leonardo Mariga",
    author_email="leomariga@gmail.com",
    description="A test using CPP files on a python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leomariga/libtest_python_cpp",
    packages=setuptools.find_packages(),
    keywords='test',
    ext_modules=extensions,
    cmdclass={"build_ext": NoSuffixBuilder},
    project_urls={
        'Documentation': 'https://github.com/leomariga/libtest_python_cpp',
        'Source': 'https://github.com/leomariga/libtest_python_cpp',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
