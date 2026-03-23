from setuptools import setup
setup(
    name='cli-anything-knockout',
    version='1.0.0',
    packages=['cli_anything.knockout'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-knockout=cli_anything.knockout:cli']},
)
