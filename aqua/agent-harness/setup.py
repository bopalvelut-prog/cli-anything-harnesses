from setuptools import setup
setup(
    name='cli-anything-aqua',
    version='1.0.0',
    packages=['cli_anything.aqua'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aqua=cli_anything.aqua:cli']},
)
