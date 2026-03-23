from setuptools import setup
setup(
    name='cli-anything-mullvad',
    version='1.0.0',
    packages=['cli_anything.mullvad'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mullvad=cli_anything.mullvad:cli']},
)
