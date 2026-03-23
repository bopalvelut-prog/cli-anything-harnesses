from setuptools import setup
setup(
    name='cli-anything-treatment',
    version='1.0.0',
    packages=['cli_anything.treatment'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-treatment=cli_anything.treatment:cli']},
)
