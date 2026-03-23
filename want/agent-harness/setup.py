from setuptools import setup
setup(
    name='cli-anything-want',
    version='1.0.0',
    packages=['cli_anything.want'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-want=cli_anything.want:cli']},
)
