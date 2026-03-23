from setuptools import setup
setup(
    name='cli-anything-runner',
    version='1.0.0',
    packages=['cli_anything.runner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-runner=cli_anything.runner:cli']},
)
