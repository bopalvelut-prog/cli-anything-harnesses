from setuptools import setup
setup(
    name='cli-anything-stackblitz',
    version='1.0.0',
    packages=['cli_anything.stackblitz'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stackblitz=cli_anything.stackblitz:cli']},
)
