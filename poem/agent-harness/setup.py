from setuptools import setup
setup(
    name='cli-anything-poem',
    version='1.0.0',
    packages=['cli_anything.poem'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-poem=cli_anything.poem:cli']},
)
