from setuptools import setup
setup(
    name='cli-anything-netbox',
    version='1.0.0',
    packages=['cli_anything.netbox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-netbox=cli_anything.netbox:cli']},
)
