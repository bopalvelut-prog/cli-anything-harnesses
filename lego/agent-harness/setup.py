from setuptools import setup
setup(
    name='cli-anything-lego',
    version='1.0.0',
    packages=['cli_anything.lego'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lego=cli_anything.lego:cli']},
)
