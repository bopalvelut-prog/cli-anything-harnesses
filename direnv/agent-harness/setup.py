from setuptools import setup
setup(
    name='cli-anything-direnv',
    version='1.0.0',
    packages=['cli_anything.direnv'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-direnv=cli_anything.direnv:cli']},
)
