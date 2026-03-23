from setuptools import setup
setup(
    name='cli-anything-stump',
    version='1.0.0',
    packages=['cli_anything.stump'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stump=cli_anything.stump:cli']},
)
