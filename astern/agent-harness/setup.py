from setuptools import setup
setup(
    name='cli-anything-astern',
    version='1.0.0',
    packages=['cli_anything.astern'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-astern=cli_anything.astern:cli']},
)
