from setuptools import setup
setup(
    name='cli-anything-medium',
    version='1.0.0',
    packages=['cli_anything.medium'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-medium=cli_anything.medium:cli']},
)
