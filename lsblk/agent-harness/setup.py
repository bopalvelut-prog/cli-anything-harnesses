from setuptools import setup
setup(
    name='cli-anything-lsblk',
    version='1.0.0',
    packages=['cli_anything.lsblk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lsblk=cli_anything.lsblk:cli']},
)
