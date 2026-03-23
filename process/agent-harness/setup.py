from setuptools import setup
setup(
    name='cli-anything-process',
    version='1.0.0',
    packages=['cli_anything.process'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-process=cli_anything.process:cli']},
)
