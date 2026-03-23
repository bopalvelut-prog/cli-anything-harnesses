from setuptools import setup
setup(
    name='cli-anything-valid',
    version='1.0.0',
    packages=['cli_anything.valid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-valid=cli_anything.valid:cli']},
)
