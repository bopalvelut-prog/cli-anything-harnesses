from setuptools import setup
setup(
    name='cli-anything-sonobuoy',
    version='1.0.0',
    packages=['cli_anything.sonobuoy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sonobuoy=cli_anything.sonobuoy:cli']},
)
