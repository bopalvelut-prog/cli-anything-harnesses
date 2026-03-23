from setuptools import setup
setup(
    name='cli-anything-fontconfig',
    version='1.0.0',
    packages=['cli_anything.fontconfig'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fontconfig=cli_anything.fontconfig:cli']},
)
