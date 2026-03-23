from setuptools import setup
setup(
    name='cli-anything-honest',
    version='1.0.0',
    packages=['cli_anything.honest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-honest=cli_anything.honest:cli']},
)
