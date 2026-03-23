from setuptools import setup
setup(
    name='cli-anything-thinking',
    version='1.0.0',
    packages=['cli_anything.thinking'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thinking=cli_anything.thinking:cli']},
)
