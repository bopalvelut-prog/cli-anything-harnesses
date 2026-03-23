from setuptools import setup
setup(
    name='cli-anything-cry',
    version='1.0.0',
    packages=['cli_anything.cry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cry=cli_anything.cry:cli']},
)
