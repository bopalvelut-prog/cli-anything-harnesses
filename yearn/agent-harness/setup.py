from setuptools import setup
setup(
    name='cli-anything-yearn',
    version='1.0.0',
    packages=['cli_anything.yearn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yearn=cli_anything.yearn:cli']},
)
