from setuptools import setup
setup(
    name='cli-anything-scientific',
    version='1.0.0',
    packages=['cli_anything.scientific'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scientific=cli_anything.scientific:cli']},
)
