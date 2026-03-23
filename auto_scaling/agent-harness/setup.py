from setuptools import setup
setup(
    name='cli-anything-auto_scaling',
    version='1.0.0',
    packages=['cli_anything.auto_scaling'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-auto_scaling=cli_anything.auto_scaling:cli']},
)
