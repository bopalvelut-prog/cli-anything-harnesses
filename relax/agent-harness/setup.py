from setuptools import setup
setup(
    name='cli-anything-relax',
    version='1.0.0',
    packages=['cli_anything.relax'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-relax=cli_anything.relax:cli']},
)
