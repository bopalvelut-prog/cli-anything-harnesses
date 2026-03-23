from setuptools import setup
setup(
    name='cli-anything-opensuse',
    version='1.0.0',
    packages=['cli_anything.opensuse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opensuse=cli_anything.opensuse:cli']},
)
