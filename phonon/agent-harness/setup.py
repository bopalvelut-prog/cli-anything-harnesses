from setuptools import setup
setup(
    name='cli-anything-phonon',
    version='1.0.0',
    packages=['cli_anything.phonon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-phonon=cli_anything.phonon:cli']},
)
