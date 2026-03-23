from setuptools import setup
setup(
    name='cli-anything-potential',
    version='1.0.0',
    packages=['cli_anything.potential'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-potential=cli_anything.potential:cli']},
)
