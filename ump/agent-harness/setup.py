from setuptools import setup
setup(
    name='cli-anything-ump',
    version='1.0.0',
    packages=['cli_anything.ump'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ump=cli_anything.ump:cli']},
)
