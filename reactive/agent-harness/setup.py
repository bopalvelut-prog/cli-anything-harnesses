from setuptools import setup
setup(
    name='cli-anything-reactive',
    version='1.0.0',
    packages=['cli_anything.reactive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reactive=cli_anything.reactive:cli']},
)
