from setuptools import setup
setup(
    name='cli-anything-replicate',
    version='1.0.0',
    packages=['cli_anything.replicate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-replicate=cli_anything.replicate:cli']},
)
