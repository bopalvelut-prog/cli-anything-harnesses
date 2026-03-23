from setuptools import setup
setup(
    name='cli-anything-film',
    version='1.0.0',
    packages=['cli_anything.film'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-film=cli_anything.film:cli']},
)
