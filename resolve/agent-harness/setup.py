from setuptools import setup
setup(
    name='cli-anything-resolve',
    version='1.0.0',
    packages=['cli_anything.resolve'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-resolve=cli_anything.resolve:cli']},
)
