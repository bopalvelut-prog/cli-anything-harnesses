from setuptools import setup
setup(
    name='cli-anything-aspect',
    version='1.0.0',
    packages=['cli_anything.aspect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aspect=cli_anything.aspect:cli']},
)
