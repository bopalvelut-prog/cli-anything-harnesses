from setuptools import setup
setup(
    name='cli-anything-past',
    version='1.0.0',
    packages=['cli_anything.past'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-past=cli_anything.past:cli']},
)
