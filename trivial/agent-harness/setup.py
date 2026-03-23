from setuptools import setup
setup(
    name='cli-anything-trivial',
    version='1.0.0',
    packages=['cli_anything.trivial'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trivial=cli_anything.trivial:cli']},
)
