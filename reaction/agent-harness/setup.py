from setuptools import setup
setup(
    name='cli-anything-reaction',
    version='1.0.0',
    packages=['cli_anything.reaction'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reaction=cli_anything.reaction:cli']},
)
