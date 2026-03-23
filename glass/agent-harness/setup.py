from setuptools import setup
setup(
    name='cli-anything-glass',
    version='1.0.0',
    packages=['cli_anything.glass'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-glass=cli_anything.glass:cli']},
)
