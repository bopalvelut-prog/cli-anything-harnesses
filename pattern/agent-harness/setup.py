from setuptools import setup
setup(
    name='cli-anything-pattern',
    version='1.0.0',
    packages=['cli_anything.pattern'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pattern=cli_anything.pattern:cli']},
)
