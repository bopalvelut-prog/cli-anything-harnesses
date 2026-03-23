from setuptools import setup
setup(
    name='cli-anything-multimedia',
    version='1.0.0',
    packages=['cli_anything.multimedia'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-multimedia=cli_anything.multimedia:cli']},
)
