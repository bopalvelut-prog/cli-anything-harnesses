from setuptools import setup
setup(
    name='cli-anything-gsl',
    version='1.0.0',
    packages=['cli_anything.gsl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gsl=cli_anything.gsl:cli']},
)
