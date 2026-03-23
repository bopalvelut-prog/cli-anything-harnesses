from setuptools import setup
setup(
    name='cli-anything-pine',
    version='1.0.0',
    packages=['cli_anything.pine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pine=cli_anything.pine:cli']},
)
