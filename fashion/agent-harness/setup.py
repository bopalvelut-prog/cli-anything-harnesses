from setuptools import setup
setup(
    name='cli-anything-fashion',
    version='1.0.0',
    packages=['cli_anything.fashion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fashion=cli_anything.fashion:cli']},
)
