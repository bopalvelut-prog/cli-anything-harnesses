from setuptools import setup
setup(
    name='cli-anything-injective',
    version='1.0.0',
    packages=['cli_anything.injective'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-injective=cli_anything.injective:cli']},
)
