from setuptools import setup
setup(
    name='cli-anything-ponyc',
    version='1.0.0',
    packages=['cli_anything.ponyc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ponyc=cli_anything.ponyc:cli']},
)
