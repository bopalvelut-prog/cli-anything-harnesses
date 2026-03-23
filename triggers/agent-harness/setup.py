from setuptools import setup
setup(
    name='cli-anything-triggers',
    version='1.0.0',
    packages=['cli_anything.triggers'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-triggers=cli_anything.triggers:cli']},
)
