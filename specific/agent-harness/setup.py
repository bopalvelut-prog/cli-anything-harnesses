from setuptools import setup
setup(
    name='cli-anything-specific',
    version='1.0.0',
    packages=['cli_anything.specific'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-specific=cli_anything.specific:cli']},
)
