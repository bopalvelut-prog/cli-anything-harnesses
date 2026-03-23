from setuptools import setup
setup(
    name='cli-anything-unsafe',
    version='1.0.0',
    packages=['cli_anything.unsafe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unsafe=cli_anything.unsafe:cli']},
)
