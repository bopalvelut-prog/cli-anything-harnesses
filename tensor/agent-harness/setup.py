from setuptools import setup
setup(
    name='cli-anything-tensor',
    version='1.0.0',
    packages=['cli_anything.tensor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tensor=cli_anything.tensor:cli']},
)
