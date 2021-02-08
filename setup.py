import setuptools
from setuptools import setup, find_packages, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()


extensions = [Extension("pyRANSAC3D.core",
                        ["src/library.c"],
                        depends=["src/library.h"],
                        include_dirs=["src"],),]

setuptools.setup(
    name="lib_cpp_python_test_", # Replace with your own username
    version="0.0.1",
    author="Leonardo Mariga",
    author_email="leomariga@gmail.com",
    description="A test using CPP files on a python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leomariga/libtest_python_cpp",
    packages=setuptools.find_packages(),
    keywords='test',
    ext_modules=extensions,
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
