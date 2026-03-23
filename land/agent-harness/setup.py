from setuptools import setup
setup(
    name='cli-anything-land',
    version='1.0.0',
    packages=['cli_anything.land'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-land=cli_anything.land:cli']},
)
