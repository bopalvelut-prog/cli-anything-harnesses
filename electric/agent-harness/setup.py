from setuptools import setup
setup(
    name='cli-anything-electric',
    version='1.0.0',
    packages=['cli_anything.electric'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-electric=cli_anything.electric:cli']},
)
