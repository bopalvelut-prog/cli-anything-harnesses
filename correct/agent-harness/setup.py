from setuptools import setup
setup(
    name='cli-anything-correct',
    version='1.0.0',
    packages=['cli_anything.correct'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-correct=cli_anything.correct:cli']},
)
