from setuptools import setup, find_packages
from cli.core.version import get_version

VERSION = get_version()

f = open("README.md", "r")
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name="mjw",
    version=VERSION,
    description="Moraj Lab workspace manager cli app",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Morteza Jamali",
    author_email="mortezajamali4241@gmail.com",
    url="https://github.com/morajlab/workspace",
    license="MIT",
    packages=find_packages(exclude=["ez_setup", "tests*"]),
    package_data={"cli": ["templates/*"]},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        mjw = cli.main:main
    """,
)
