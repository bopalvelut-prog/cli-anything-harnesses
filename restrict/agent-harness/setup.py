from setuptools import setup
setup(
    name='cli-anything-restrict',
    version='1.0.0',
    packages=['cli_anything.restrict'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-restrict=cli_anything.restrict:cli']},
)
