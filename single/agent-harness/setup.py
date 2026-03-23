from setuptools import setup
setup(
    name='cli-anything-single',
    version='1.0.0',
    packages=['cli_anything.single'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-single=cli_anything.single:cli']},
)
