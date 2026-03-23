from setuptools import setup
setup(
    name='cli-anything-exhibit',
    version='1.0.0',
    packages=['cli_anything.exhibit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-exhibit=cli_anything.exhibit:cli']},
)
