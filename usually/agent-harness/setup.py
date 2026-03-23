from setuptools import setup
setup(
    name='cli-anything-usually',
    version='1.0.0',
    packages=['cli_anything.usually'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-usually=cli_anything.usually:cli']},
)
