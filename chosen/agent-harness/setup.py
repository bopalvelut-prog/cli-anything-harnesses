from setuptools import setup
setup(
    name='cli-anything-chosen',
    version='1.0.0',
    packages=['cli_anything.chosen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chosen=cli_anything.chosen:cli']},
)
