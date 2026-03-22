from setuptools import setup
setup(
    name='cli-anything-slack',
    version='1.0.0',
    packages=['cli_anything.slack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slack=cli_anything.slack:cli']},
)
