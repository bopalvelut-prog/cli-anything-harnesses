from setuptools import setup
setup(
    name='cli-anything-grandmother',
    version='1.0.0',
    packages=['cli_anything.grandmother'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grandmother=cli_anything.grandmother:cli']},
)
