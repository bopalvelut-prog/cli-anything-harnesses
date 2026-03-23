from setuptools import setup
setup(
    name='cli-anything-empty',
    version='1.0.0',
    packages=['cli_anything.empty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-empty=cli_anything.empty:cli']},
)
