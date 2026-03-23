from setuptools import setup
setup(
    name='cli-anything-effect',
    version='1.0.0',
    packages=['cli_anything.effect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-effect=cli_anything.effect:cli']},
)
