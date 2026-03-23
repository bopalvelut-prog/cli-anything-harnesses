from setuptools import setup
setup(
    name='cli-anything-sometimes',
    version='1.0.0',
    packages=['cli_anything.sometimes'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sometimes=cli_anything.sometimes:cli']},
)
