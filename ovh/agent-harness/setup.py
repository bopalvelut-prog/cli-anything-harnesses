from setuptools import setup
setup(
    name='cli-anything-ovh',
    version='1.0.0',
    packages=['cli_anything.ovh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ovh=cli_anything.ovh:cli']},
)
