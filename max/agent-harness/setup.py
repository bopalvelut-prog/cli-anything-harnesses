from setuptools import setup
setup(
    name='cli-anything-max',
    version='1.0.0',
    packages=['cli_anything.max'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-max=cli_anything.max:cli']},
)
