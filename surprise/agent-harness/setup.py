from setuptools import setup
setup(
    name='cli-anything-surprise',
    version='1.0.0',
    packages=['cli_anything.surprise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-surprise=cli_anything.surprise:cli']},
)
