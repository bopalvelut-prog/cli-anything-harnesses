from setuptools import setup
setup(
    name='cli-anything-grandfather',
    version='1.0.0',
    packages=['cli_anything.grandfather'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grandfather=cli_anything.grandfather:cli']},
)
