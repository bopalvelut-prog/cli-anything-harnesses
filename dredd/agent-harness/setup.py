from setuptools import setup
setup(
    name='cli-anything-dredd',
    version='1.0.0',
    packages=['cli_anything.dredd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dredd=cli_anything.dredd:cli']},
)
