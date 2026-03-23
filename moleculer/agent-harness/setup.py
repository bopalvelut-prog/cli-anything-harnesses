from setuptools import setup
setup(
    name='cli-anything-moleculer',
    version='1.0.0',
    packages=['cli_anything.moleculer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-moleculer=cli_anything.moleculer:cli']},
)
