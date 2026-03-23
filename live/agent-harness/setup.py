from setuptools import setup
setup(
    name='cli-anything-live',
    version='1.0.0',
    packages=['cli_anything.live'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-live=cli_anything.live:cli']},
)
