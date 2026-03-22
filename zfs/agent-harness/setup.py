from setuptools import setup
setup(
    name='cli-anything-zfs',
    version='1.0.0',
    packages=['cli_anything.zfs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zfs=cli_anything.zfs:cli']},
)
