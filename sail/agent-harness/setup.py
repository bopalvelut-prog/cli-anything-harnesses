from setuptools import setup
setup(
    name='cli-anything-sail',
    version='1.0.0',
    packages=['cli_anything.sail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sail=cli_anything.sail:cli']},
)
