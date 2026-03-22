from setuptools import setup
setup(
    name='cli-anything-ceph',
    version='1.0.0',
    packages=['cli_anything.ceph'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ceph=cli_anything.ceph:cli']},
)
