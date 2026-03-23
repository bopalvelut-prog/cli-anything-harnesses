from setuptools import setup
setup(
    name='cli-anything-clearlinux',
    version='1.0.0',
    packages=['cli_anything.clearlinux'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clearlinux=cli_anything.clearlinux:cli']},
)
