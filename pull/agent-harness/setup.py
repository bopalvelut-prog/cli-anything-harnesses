from setuptools import setup
setup(
    name='cli-anything-pull',
    version='1.0.0',
    packages=['cli_anything.pull'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pull=cli_anything.pull:cli']},
)
