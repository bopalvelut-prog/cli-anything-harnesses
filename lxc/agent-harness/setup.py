from setuptools import setup
setup(
    name='cli-anything-lxc',
    version='1.0.0',
    packages=['cli_anything.lxc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lxc=cli_anything.lxc:cli']},
)
