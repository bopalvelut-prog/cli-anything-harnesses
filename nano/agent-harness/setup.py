from setuptools import setup
setup(
    name='cli-anything-nano',
    version='1.0.0',
    packages=['cli_anything.nano'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nano=cli_anything.nano:cli']},
)
