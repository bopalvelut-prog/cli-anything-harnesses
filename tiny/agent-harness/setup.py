from setuptools import setup
setup(
    name='cli-anything-tiny',
    version='1.0.0',
    packages=['cli_anything.tiny'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tiny=cli_anything.tiny:cli']},
)
