from setuptools import setup
setup(
    name='cli-anything-archlinux',
    version='1.0.0',
    packages=['cli_anything.archlinux'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-archlinux=cli_anything.archlinux:cli']},
)
