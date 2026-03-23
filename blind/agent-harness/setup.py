from setuptools import setup
setup(
    name='cli-anything-blind',
    version='1.0.0',
    packages=['cli_anything.blind'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blind=cli_anything.blind:cli']},
)
