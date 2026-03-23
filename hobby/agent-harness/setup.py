from setuptools import setup
setup(
    name='cli-anything-hobby',
    version='1.0.0',
    packages=['cli_anything.hobby'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hobby=cli_anything.hobby:cli']},
)
