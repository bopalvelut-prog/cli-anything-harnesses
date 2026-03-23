from setuptools import setup
setup(
    name='cli-anything-nxdomain',
    version='1.0.0',
    packages=['cli_anything.nxdomain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nxdomain=cli_anything.nxdomain:cli']},
)
