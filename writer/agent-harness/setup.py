from setuptools import setup
setup(
    name='cli-anything-writer',
    version='1.0.0',
    packages=['cli_anything.writer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-writer=cli_anything.writer:cli']},
)
