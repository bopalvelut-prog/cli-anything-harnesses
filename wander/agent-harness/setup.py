from setuptools import setup
setup(
    name='cli-anything-wander',
    version='1.0.0',
    packages=['cli_anything.wander'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wander=cli_anything.wander:cli']},
)
