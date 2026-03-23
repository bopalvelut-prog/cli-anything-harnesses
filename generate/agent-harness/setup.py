from setuptools import setup
setup(
    name='cli-anything-generate',
    version='1.0.0',
    packages=['cli_anything.generate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-generate=cli_anything.generate:cli']},
)
