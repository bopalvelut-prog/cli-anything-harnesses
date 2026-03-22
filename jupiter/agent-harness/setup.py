from setuptools import setup
setup(
    name='cli-anything-jupiter',
    version='1.0.0',
    packages=['cli_anything.jupiter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jupiter=cli_anything.jupiter:cli']},
)
