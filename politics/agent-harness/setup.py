from setuptools import setup
setup(
    name='cli-anything-politics',
    version='1.0.0',
    packages=['cli_anything.politics'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-politics=cli_anything.politics:cli']},
)
