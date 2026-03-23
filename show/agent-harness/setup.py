from setuptools import setup
setup(
    name='cli-anything-show',
    version='1.0.0',
    packages=['cli_anything.show'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-show=cli_anything.show:cli']},
)
