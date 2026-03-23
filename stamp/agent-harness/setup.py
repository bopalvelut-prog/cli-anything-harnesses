from setuptools import setup
setup(
    name='cli-anything-stamp',
    version='1.0.0',
    packages=['cli_anything.stamp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stamp=cli_anything.stamp:cli']},
)
