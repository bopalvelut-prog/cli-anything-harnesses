from setuptools import setup
setup(
    name='cli-anything-prove',
    version='1.0.0',
    packages=['cli_anything.prove'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prove=cli_anything.prove:cli']},
)
