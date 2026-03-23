from setuptools import setup
setup(
    name='cli-anything-remember',
    version='1.0.0',
    packages=['cli_anything.remember'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-remember=cli_anything.remember:cli']},
)
