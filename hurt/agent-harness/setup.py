from setuptools import setup
setup(
    name='cli-anything-hurt',
    version='1.0.0',
    packages=['cli_anything.hurt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hurt=cli_anything.hurt:cli']},
)
