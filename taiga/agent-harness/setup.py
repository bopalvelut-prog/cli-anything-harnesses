from setuptools import setup
setup(
    name='cli-anything-taiga',
    version='1.0.0',
    packages=['cli_anything.taiga'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-taiga=cli_anything.taiga:cli']},
)
