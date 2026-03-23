from setuptools import setup
setup(
    name='cli-anything-man',
    version='1.0.0',
    packages=['cli_anything.man'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-man=cli_anything.man:cli']},
)
