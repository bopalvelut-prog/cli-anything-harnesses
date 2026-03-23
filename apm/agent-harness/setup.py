from setuptools import setup
setup(
    name='cli-anything-apm',
    version='1.0.0',
    packages=['cli_anything.apm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apm=cli_anything.apm:cli']},
)
