from setuptools import setup
setup(
    name='cli-anything-willing',
    version='1.0.0',
    packages=['cli_anything.willing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-willing=cli_anything.willing:cli']},
)
