from setuptools import setup
setup(
    name='cli-anything-toddy',
    version='1.0.0',
    packages=['cli_anything.toddy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-toddy=cli_anything.toddy:cli']},
)
