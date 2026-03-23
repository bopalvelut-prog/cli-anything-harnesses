from setuptools import setup
setup(
    name='cli-anything-hal',
    version='1.0.0',
    packages=['cli_anything.hal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hal=cli_anything.hal:cli']},
)
