from setuptools import setup
setup(
    name='cli-anything-goal',
    version='1.0.0',
    packages=['cli_anything.goal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-goal=cli_anything.goal:cli']},
)
