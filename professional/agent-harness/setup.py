from setuptools import setup
setup(
    name='cli-anything-professional',
    version='1.0.0',
    packages=['cli_anything.professional'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-professional=cli_anything.professional:cli']},
)
