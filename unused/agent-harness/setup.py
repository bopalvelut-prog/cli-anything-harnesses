from setuptools import setup
setup(
    name='cli-anything-unused',
    version='1.0.0',
    packages=['cli_anything.unused'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unused=cli_anything.unused:cli']},
)
