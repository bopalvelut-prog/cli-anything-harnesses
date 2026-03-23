from setuptools import setup
setup(
    name='cli-anything-genre',
    version='1.0.0',
    packages=['cli_anything.genre'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-genre=cli_anything.genre:cli']},
)
