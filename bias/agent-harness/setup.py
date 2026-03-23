from setuptools import setup
setup(
    name='cli-anything-bias',
    version='1.0.0',
    packages=['cli_anything.bias'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bias=cli_anything.bias:cli']},
)
