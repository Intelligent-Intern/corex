"""
Setup script for the corex package.
"""

from setuptools import setup, find_packages

setup(
    name="corex",
    version="0.1.0",
    description="CoreX is a modular, standardized interface framework for Python applications. It provides a consistent API for essential cross-cutting concerns such as storage, caching, messaging, security, databases, event processing, AI, and more.",
    author="Jochen Schultz",
    author_email="js@intelligent-intern.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
