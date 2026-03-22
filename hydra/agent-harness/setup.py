from setuptools import setup
setup(
    name='cli-anything-hydra',
    version='1.0.0',
    packages=['cli_anything.hydra'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hydra=cli_anything.hydra:cli']},
)
