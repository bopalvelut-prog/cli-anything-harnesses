from setuptools import setup
setup(
    name='cli-anything-tensorrt',
    version='1.0.0',
    packages=['cli_anything.tensorrt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tensorrt=cli_anything.tensorrt:cli']},
)
