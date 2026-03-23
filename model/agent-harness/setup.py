from setuptools import setup
setup(
    name='cli-anything-model',
    version='1.0.0',
    packages=['cli_anything.model'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-model=cli_anything.model:cli']},
)
