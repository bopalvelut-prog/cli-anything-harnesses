from setuptools import setup
setup(
    name='cli-anything-xcode',
    version='1.0.0',
    packages=['cli_anything.xcode'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xcode=cli_anything.xcode:cli']},
)
