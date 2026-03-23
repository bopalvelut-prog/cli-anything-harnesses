from setuptools import setup
setup(
    name='cli-anything-semver',
    version='1.0.0',
    packages=['cli_anything.semver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-semver=cli_anything.semver:cli']},
)
