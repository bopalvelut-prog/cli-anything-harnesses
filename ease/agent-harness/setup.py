from setuptools import setup
setup(
    name='cli-anything-ease',
    version='1.0.0',
    packages=['cli_anything.ease'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ease=cli_anything.ease:cli']},
)
