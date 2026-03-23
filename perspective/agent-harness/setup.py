from setuptools import setup
setup(
    name='cli-anything-perspective',
    version='1.0.0',
    packages=['cli_anything.perspective'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-perspective=cli_anything.perspective:cli']},
)
