from setuptools import setup
setup(
    name='cli-anything-neo',
    version='1.0.0',
    packages=['cli_anything.neo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-neo=cli_anything.neo:cli']},
)
