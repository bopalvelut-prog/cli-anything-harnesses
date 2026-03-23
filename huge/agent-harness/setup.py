from setuptools import setup
setup(
    name='cli-anything-huge',
    version='1.0.0',
    packages=['cli_anything.huge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-huge=cli_anything.huge:cli']},
)
