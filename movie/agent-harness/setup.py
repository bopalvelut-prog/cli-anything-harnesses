from setuptools import setup
setup(
    name='cli-anything-movie',
    version='1.0.0',
    packages=['cli_anything.movie'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-movie=cli_anything.movie:cli']},
)
