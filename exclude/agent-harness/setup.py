from setuptools import setup
setup(
    name='cli-anything-exclude',
    version='1.0.0',
    packages=['cli_anything.exclude'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-exclude=cli_anything.exclude:cli']},
)
