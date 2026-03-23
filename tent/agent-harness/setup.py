from setuptools import setup
setup(
    name='cli-anything-tent',
    version='1.0.0',
    packages=['cli_anything.tent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tent=cli_anything.tent:cli']},
)
