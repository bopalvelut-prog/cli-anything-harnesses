from setuptools import setup
setup(
    name='cli-anything-alveo',
    version='1.0.0',
    packages=['cli_anything.alveo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alveo=cli_anything.alveo:cli']},
)
