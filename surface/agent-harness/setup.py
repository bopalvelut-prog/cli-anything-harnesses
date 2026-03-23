from setuptools import setup
setup(
    name='cli-anything-surface',
    version='1.0.0',
    packages=['cli_anything.surface'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-surface=cli_anything.surface:cli']},
)
