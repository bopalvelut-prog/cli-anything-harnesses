from setuptools import setup
setup(
    name='cli-anything-biology',
    version='1.0.0',
    packages=['cli_anything.biology'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-biology=cli_anything.biology:cli']},
)
