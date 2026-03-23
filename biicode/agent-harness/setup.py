from setuptools import setup
setup(
    name='cli-anything-biicode',
    version='1.0.0',
    packages=['cli_anything.biicode'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-biicode=cli_anything.biicode:cli']},
)
