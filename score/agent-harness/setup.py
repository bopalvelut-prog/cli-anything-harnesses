from setuptools import setup
setup(
    name='cli-anything-score',
    version='1.0.0',
    packages=['cli_anything.score'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-score=cli_anything.score:cli']},
)
