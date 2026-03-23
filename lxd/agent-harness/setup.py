from setuptools import setup
setup(
    name='cli-anything-lxd',
    version='1.0.0',
    packages=['cli_anything.lxd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lxd=cli_anything.lxd:cli']},
)
