from setuptools import setup
setup(
    name='cli-anything-cause',
    version='1.0.0',
    packages=['cli_anything.cause'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cause=cli_anything.cause:cli']},
)
