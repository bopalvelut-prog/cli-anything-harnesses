from setuptools import setup
setup(
    name='cli-anything-isolate',
    version='1.0.0',
    packages=['cli_anything.isolate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-isolate=cli_anything.isolate:cli']},
)
