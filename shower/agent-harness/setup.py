from setuptools import setup
setup(
    name='cli-anything-shower',
    version='1.0.0',
    packages=['cli_anything.shower'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shower=cli_anything.shower:cli']},
)
