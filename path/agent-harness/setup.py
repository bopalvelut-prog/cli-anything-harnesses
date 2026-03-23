from setuptools import setup
setup(
    name='cli-anything-path',
    version='1.0.0',
    packages=['cli_anything.path'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-path=cli_anything.path:cli']},
)
