from setuptools import setup
setup(
    name='cli-anything-bar',
    version='1.0.0',
    packages=['cli_anything.bar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bar=cli_anything.bar:cli']},
)
