from setuptools import setup
setup(
    name='cli-anything-chord',
    version='1.0.0',
    packages=['cli_anything.chord'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chord=cli_anything.chord:cli']},
)
