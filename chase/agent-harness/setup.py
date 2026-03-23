from setuptools import setup
setup(
    name='cli-anything-chase',
    version='1.0.0',
    packages=['cli_anything.chase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chase=cli_anything.chase:cli']},
)
