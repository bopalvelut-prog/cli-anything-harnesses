from setuptools import setup
setup(
    name='cli-anything-black',
    version='1.0.0',
    packages=['cli_anything.black'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-black=cli_anything.black:cli']},
)
