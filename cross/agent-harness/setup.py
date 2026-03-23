from setuptools import setup
setup(
    name='cli-anything-cross',
    version='1.0.0',
    packages=['cli_anything.cross'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cross=cli_anything.cross:cli']},
)
