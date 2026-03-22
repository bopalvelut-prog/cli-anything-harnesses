from setuptools import setup
setup(
    name='cli-anything-latex',
    version='1.0.0',
    packages=['cli_anything.latex'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-latex=cli_anything.latex:cli']},
)
