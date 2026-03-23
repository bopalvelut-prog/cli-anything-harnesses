from setuptools import setup
setup(
    name='cli-anything-doctor',
    version='1.0.0',
    packages=['cli_anything.doctor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-doctor=cli_anything.doctor:cli']},
)
