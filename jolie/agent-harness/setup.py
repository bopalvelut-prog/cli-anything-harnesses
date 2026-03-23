from setuptools import setup
setup(
    name='cli-anything-jolie',
    version='1.0.0',
    packages=['cli_anything.jolie'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jolie=cli_anything.jolie:cli']},
)
