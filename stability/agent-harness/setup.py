from setuptools import setup
setup(
    name='cli-anything-stability',
    version='1.0.0',
    packages=['cli_anything.stability'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stability=cli_anything.stability:cli']},
)
