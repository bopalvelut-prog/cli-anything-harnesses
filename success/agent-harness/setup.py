from setuptools import setup
setup(
    name='cli-anything-success',
    version='1.0.0',
    packages=['cli_anything.success'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-success=cli_anything.success:cli']},
)
