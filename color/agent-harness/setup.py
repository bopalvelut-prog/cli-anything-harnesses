from setuptools import setup
setup(
    name='cli-anything-color',
    version='1.0.0',
    packages=['cli_anything.color'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-color=cli_anything.color:cli']},
)
