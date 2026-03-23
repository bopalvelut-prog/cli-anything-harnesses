from setuptools import setup
setup(
    name='cli-anything-cssnano',
    version='1.0.0',
    packages=['cli_anything.cssnano'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cssnano=cli_anything.cssnano:cli']},
)
