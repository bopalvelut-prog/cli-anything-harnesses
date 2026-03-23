from setuptools import setup
setup(
    name='cli-anything-highlight',
    version='1.0.0',
    packages=['cli_anything.highlight'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-highlight=cli_anything.highlight:cli']},
)
