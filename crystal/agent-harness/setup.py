from setuptools import setup
setup(
    name='cli-anything-crystal',
    version='1.0.0',
    packages=['cli_anything.crystal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crystal=cli_anything.crystal:cli']},
)
