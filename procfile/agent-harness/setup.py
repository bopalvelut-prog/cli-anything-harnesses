from setuptools import setup
setup(
    name='cli-anything-procfile',
    version='1.0.0',
    packages=['cli_anything.procfile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-procfile=cli_anything.procfile:cli']},
)
