from setuptools import setup
setup(
    name='cli-anything-openstack',
    version='1.0.0',
    packages=['cli_anything.openstack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openstack=cli_anything.openstack:cli']},
)
