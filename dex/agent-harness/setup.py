from setuptools import setup
setup(
    name='cli-anything-dex',
    version='1.0.0',
    packages=['cli_anything.dex'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dex=cli_anything.dex:cli']},
)
