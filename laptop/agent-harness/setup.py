from setuptools import setup
setup(
    name='cli-anything-laptop',
    version='1.0.0',
    packages=['cli_anything.laptop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-laptop=cli_anything.laptop:cli']},
)
