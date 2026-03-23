from setuptools import setup
setup(
    name='cli-anything-level',
    version='1.0.0',
    packages=['cli_anything.level'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-level=cli_anything.level:cli']},
)
