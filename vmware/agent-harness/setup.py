from setuptools import setup
setup(
    name='cli-anything-vmware',
    version='1.0.0',
    packages=['cli_anything.vmware'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vmware=cli_anything.vmware:cli']},
)
