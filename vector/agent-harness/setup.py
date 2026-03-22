from setuptools import setup
setup(
    name='cli-anything-vector',
    version='1.0.0',
    packages=['cli_anything.vector'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vector=cli_anything.vector:cli']},
)
