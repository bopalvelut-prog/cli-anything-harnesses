from setuptools import setup
setup(
    name='cli-anything-powerdns',
    version='1.0.0',
    packages=['cli_anything.powerdns'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-powerdns=cli_anything.powerdns:cli']},
)
