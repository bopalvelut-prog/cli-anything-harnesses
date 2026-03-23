from setuptools import setup
setup(
    name='cli-anything-interpret',
    version='1.0.0',
    packages=['cli_anything.interpret'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-interpret=cli_anything.interpret:cli']},
)
