from setuptools import setup
setup(
    name='cli-anything-real',
    version='1.0.0',
    packages=['cli_anything.real'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real=cli_anything.real:cli']},
)
