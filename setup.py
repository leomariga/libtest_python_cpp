import setuptools
from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext
from distutils import sysconfig
import os
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()


# class NoSuffixBuilder(build_ext):
#     def get_ext_filename(self, ext_name):
#         filename = super().get_ext_filename(ext_name)
#         suffix = sysconfig.get_config_var('EXT_SUFFIX')
#         return filename.replace(suffix, "")

module1 = Extension('testel',
                    sources = ['testel.cpp'],
                    depends=['testel.h'],
                    libraries = ["user32"], # <-- Here it is
                    optional=os.environ.get('CIBUILDWHEEL', '0') != '1')

# extensions = [Extension('lib',
#                         [os.path.join('pycpp_lib', 'cpp','lib.cpp')],
#                         depends=[os.path.join('pycpp_lib', 'cpp','lib.h')],
#                         optional=os.environ.get('CIBUILDWHEEL', '0') != '1',
#                         extra_compile_args=['/d2FH4-'] if sys.platform == 'win32' else [],
#                         include_dirs=[os.path.join('pycpp_lib', 'cpp')],),]

setuptools.setup(
    name="libcppython", # Replace with your own username
    version="0.0.8",
    author="Leonardo Mariga",
    author_email="leomariga@gmail.com",
    description="A test using CPP files on a python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leomariga/libtest_python_cpp",
    packages=setuptools.find_packages(),
    keywords='test',
    ext_modules=[module1],
    # cmdclass={"build_ext": NoSuffixBuilder},
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
