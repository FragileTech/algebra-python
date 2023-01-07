"""biogen package installation metadata."""
from importlib.machinery import SourceFileLoader
from pathlib import Path

from setuptools import find_packages, setup


version = SourceFileLoader(
    "algebra.version",
    str(Path(__file__).parent / "src" / "algebra" / "version.py"),
).load_module()

with open(Path(__file__).with_name("README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="algebra",
    description="Curso de algebra lineal master analisis de datos UMH",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    version=version.__version__,
    license="MIT",
    author="guillemdb",
    author_email="guillem.duranballester@bayer.com",
    url="https://github.com/bayer-int/biogen",
    keywords=["Machine learning", "artificial intelligence"],
    test_suite="tests",
    tests_require=["pytest>=5.3.5", "hypothesis>=5.6.0"],
    extras_require={},
    install_requires=["numpy", "einops"],
    package_data={
        "": ["README.md"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
    ],
)
