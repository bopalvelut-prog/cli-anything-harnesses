from setuptools import setup
setup(
    name='cli-anything-ipvs',
    version='1.0.0',
    packages=['cli_anything.ipvs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ipvs=cli_anything.ipvs:cli']},
)
