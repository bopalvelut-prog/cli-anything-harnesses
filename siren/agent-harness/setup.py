from setuptools import setup
setup(
    name='cli-anything-siren',
    version='1.0.0',
    packages=['cli_anything.siren'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-siren=cli_anything.siren:cli']},
)
