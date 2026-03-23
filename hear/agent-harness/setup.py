from setuptools import setup
setup(
    name='cli-anything-hear',
    version='1.0.0',
    packages=['cli_anything.hear'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hear=cli_anything.hear:cli']},
)
