from setuptools import setup
setup(
    name='cli-anything-shadow',
    version='1.0.0',
    packages=['cli_anything.shadow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shadow=cli_anything.shadow:cli']},
)
