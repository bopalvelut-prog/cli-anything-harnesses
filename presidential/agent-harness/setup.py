from setuptools import setup
setup(
    name='cli-anything-presidential',
    version='1.0.0',
    packages=['cli_anything.presidential'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-presidential=cli_anything.presidential:cli']},
)
