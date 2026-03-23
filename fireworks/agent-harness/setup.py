from setuptools import setup
setup(
    name='cli-anything-fireworks',
    version='1.0.0',
    packages=['cli_anything.fireworks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fireworks=cli_anything.fireworks:cli']},
)
