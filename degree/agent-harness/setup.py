from setuptools import setup
setup(
    name='cli-anything-degree',
    version='1.0.0',
    packages=['cli_anything.degree'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-degree=cli_anything.degree:cli']},
)
