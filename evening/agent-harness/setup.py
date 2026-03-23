from setuptools import setup
setup(
    name='cli-anything-evening',
    version='1.0.0',
    packages=['cli_anything.evening'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-evening=cli_anything.evening:cli']},
)
