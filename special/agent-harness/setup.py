from setuptools import setup
setup(
    name='cli-anything-special',
    version='1.0.0',
    packages=['cli_anything.special'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-special=cli_anything.special:cli']},
)
