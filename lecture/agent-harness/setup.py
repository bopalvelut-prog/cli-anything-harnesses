from setuptools import setup
setup(
    name='cli-anything-lecture',
    version='1.0.0',
    packages=['cli_anything.lecture'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lecture=cli_anything.lecture:cli']},
)
