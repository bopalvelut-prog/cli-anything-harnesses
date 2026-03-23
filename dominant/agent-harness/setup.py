from setuptools import setup
setup(
    name='cli-anything-dominant',
    version='1.0.0',
    packages=['cli_anything.dominant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dominant=cli_anything.dominant:cli']},
)
