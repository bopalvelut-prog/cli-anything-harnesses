from setuptools import setup
setup(
    name='cli-anything-face',
    version='1.0.0',
    packages=['cli_anything.face'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-face=cli_anything.face:cli']},
)
