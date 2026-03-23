from setuptools import setup
setup(
    name='cli-anything-waterfall',
    version='1.0.0',
    packages=['cli_anything.waterfall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-waterfall=cli_anything.waterfall:cli']},
)
