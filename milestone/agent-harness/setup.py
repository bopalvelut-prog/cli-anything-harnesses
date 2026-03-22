from setuptools import setup
setup(
    name='cli-anything-milestone',
    version='1.0.0',
    packages=['cli_anything.milestone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-milestone=cli_anything.milestone:cli']},
)
