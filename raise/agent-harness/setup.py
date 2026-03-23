from setuptools import setup
setup(
    name='cli-anything-raise',
    version='1.0.0',
    packages=['cli_anything.raise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-raise=cli_anything.raise:cli']},
)
