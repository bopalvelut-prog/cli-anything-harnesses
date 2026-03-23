from setuptools import setup
setup(
    name='cli-anything-yaml',
    version='1.0.0',
    packages=['cli_anything.yaml'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yaml=cli_anything.yaml:cli']},
)
