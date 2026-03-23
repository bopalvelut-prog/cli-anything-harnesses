from setuptools import setup
setup(
    name='cli-anything-suggest',
    version='1.0.0',
    packages=['cli_anything.suggest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-suggest=cli_anything.suggest:cli']},
)
