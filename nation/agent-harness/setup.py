from setuptools import setup
setup(
    name='cli-anything-nation',
    version='1.0.0',
    packages=['cli_anything.nation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nation=cli_anything.nation:cli']},
)
