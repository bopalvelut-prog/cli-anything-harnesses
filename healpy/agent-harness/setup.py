from setuptools import setup
setup(
    name='cli-anything-healpy',
    version='1.0.0',
    packages=['cli_anything.healpy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-healpy=cli_anything.healpy:cli']},
)
