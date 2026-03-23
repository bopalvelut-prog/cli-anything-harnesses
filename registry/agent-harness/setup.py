from setuptools import setup
setup(
    name='cli-anything-registry',
    version='1.0.0',
    packages=['cli_anything.registry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-registry=cli_anything.registry:cli']},
)
