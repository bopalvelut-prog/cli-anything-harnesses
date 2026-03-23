from setuptools import setup
setup(
    name='cli-anything-gray',
    version='1.0.0',
    packages=['cli_anything.gray'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gray=cli_anything.gray:cli']},
)
