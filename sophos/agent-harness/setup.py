from setuptools import setup
setup(
    name='cli-anything-sophos',
    version='1.0.0',
    packages=['cli_anything.sophos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sophos=cli_anything.sophos:cli']},
)
