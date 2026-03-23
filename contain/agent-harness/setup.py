from setuptools import setup
setup(
    name='cli-anything-contain',
    version='1.0.0',
    packages=['cli_anything.contain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-contain=cli_anything.contain:cli']},
)
