from setuptools import setup
setup(
    name='cli-anything-triangle',
    version='1.0.0',
    packages=['cli_anything.triangle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-triangle=cli_anything.triangle:cli']},
)
