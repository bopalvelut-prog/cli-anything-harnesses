from setuptools import setup
setup(
    name='cli-anything-wolf',
    version='1.0.0',
    packages=['cli_anything.wolf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wolf=cli_anything.wolf:cli']},
)
