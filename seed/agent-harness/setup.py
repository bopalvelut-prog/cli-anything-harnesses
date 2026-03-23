from setuptools import setup
setup(
    name='cli-anything-seed',
    version='1.0.0',
    packages=['cli_anything.seed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-seed=cli_anything.seed:cli']},
)
