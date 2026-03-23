from setuptools import setup
setup(
    name='cli-anything-visibility',
    version='1.0.0',
    packages=['cli_anything.visibility'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-visibility=cli_anything.visibility:cli']},
)
