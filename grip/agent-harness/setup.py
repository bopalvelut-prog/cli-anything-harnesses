from setuptools import setup
setup(
    name='cli-anything-grip',
    version='1.0.0',
    packages=['cli_anything.grip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grip=cli_anything.grip:cli']},
)
