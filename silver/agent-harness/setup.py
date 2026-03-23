from setuptools import setup
setup(
    name='cli-anything-silver',
    version='1.0.0',
    packages=['cli_anything.silver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-silver=cli_anything.silver:cli']},
)
