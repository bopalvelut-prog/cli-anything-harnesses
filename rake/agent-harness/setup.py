from setuptools import setup
setup(
    name='cli-anything-rake',
    version='1.0.0',
    packages=['cli_anything.rake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rake=cli_anything.rake:cli']},
)
