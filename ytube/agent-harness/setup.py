from setuptools import setup
setup(
    name='cli-anything-ytube',
    version='1.0.0',
    packages=['cli_anything.ytube'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ytube=cli_anything.ytube:cli']},
)
