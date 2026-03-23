from setuptools import setup
setup(
    name='cli-anything-dirty',
    version='1.0.0',
    packages=['cli_anything.dirty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dirty=cli_anything.dirty:cli']},
)
