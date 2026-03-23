from setuptools import setup
setup(
    name='cli-anything-freedesktop',
    version='1.0.0',
    packages=['cli_anything.freedesktop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-freedesktop=cli_anything.freedesktop:cli']},
)
