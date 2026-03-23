from setuptools import setup
setup(
    name='cli-anything-condition',
    version='1.0.0',
    packages=['cli_anything.condition'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-condition=cli_anything.condition:cli']},
)
