from setuptools import setup
setup(
    name='cli-anything-dominate',
    version='1.0.0',
    packages=['cli_anything.dominate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dominate=cli_anything.dominate:cli']},
)
