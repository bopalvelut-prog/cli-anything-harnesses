from setuptools import setup
setup(
    name='cli-anything-label',
    version='1.0.0',
    packages=['cli_anything.label'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-label=cli_anything.label:cli']},
)
