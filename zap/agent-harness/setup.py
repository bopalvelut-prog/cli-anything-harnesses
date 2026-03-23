from setuptools import setup
setup(
    name='cli-anything-zap',
    version='1.0.0',
    packages=['cli_anything.zap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zap=cli_anything.zap:cli']},
)
