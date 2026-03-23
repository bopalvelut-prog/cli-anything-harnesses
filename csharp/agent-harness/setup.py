from setuptools import setup
setup(
    name='cli-anything-csharp',
    version='1.0.0',
    packages=['cli_anything.csharp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-csharp=cli_anything.csharp:cli']},
)
