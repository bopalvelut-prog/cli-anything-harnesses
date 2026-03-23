from setuptools import setup
setup(
    name='cli-anything-segment',
    version='1.0.0',
    packages=['cli_anything.segment'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-segment=cli_anything.segment:cli']},
)
