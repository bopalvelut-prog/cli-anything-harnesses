from setuptools import setup
setup(
    name='cli-anything-warn',
    version='1.0.0',
    packages=['cli_anything.warn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-warn=cli_anything.warn:cli']},
)
