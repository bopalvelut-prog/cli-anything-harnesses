from setuptools import setup
setup(
    name='cli-anything-painter',
    version='1.0.0',
    packages=['cli_anything.painter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-painter=cli_anything.painter:cli']},
)
