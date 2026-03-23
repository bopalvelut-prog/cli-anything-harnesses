from setuptools import setup
setup(
    name='cli-anything-director',
    version='1.0.0',
    packages=['cli_anything.director'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-director=cli_anything.director:cli']},
)
