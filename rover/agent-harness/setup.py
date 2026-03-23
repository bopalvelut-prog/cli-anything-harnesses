from setuptools import setup
setup(
    name='cli-anything-rover',
    version='1.0.0',
    packages=['cli_anything.rover'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rover=cli_anything.rover:cli']},
)
