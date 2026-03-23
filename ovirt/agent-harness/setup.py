from setuptools import setup
setup(
    name='cli-anything-ovirt',
    version='1.0.0',
    packages=['cli_anything.ovirt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ovirt=cli_anything.ovirt:cli']},
)
