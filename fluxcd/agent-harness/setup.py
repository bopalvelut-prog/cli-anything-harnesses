from setuptools import setup
setup(
    name='cli-anything-fluxcd',
    version='1.0.0',
    packages=['cli_anything.fluxcd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fluxcd=cli_anything.fluxcd:cli']},
)
