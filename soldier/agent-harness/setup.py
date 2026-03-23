from setuptools import setup
setup(
    name='cli-anything-soldier',
    version='1.0.0',
    packages=['cli_anything.soldier'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-soldier=cli_anything.soldier:cli']},
)
