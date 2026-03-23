from setuptools import setup
setup(
    name='cli-anything-pipeline',
    version='1.0.0',
    packages=['cli_anything.pipeline'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pipeline=cli_anything.pipeline:cli']},
)
