from setuptools import setup
setup(
    name='cli-anything-eye',
    version='1.0.0',
    packages=['cli_anything.eye'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-eye=cli_anything.eye:cli']},
)
