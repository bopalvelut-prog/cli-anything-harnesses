from setuptools import setup
setup(
    name='cli-anything-deis',
    version='1.0.0',
    packages=['cli_anything.deis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deis=cli_anything.deis:cli']},
)
