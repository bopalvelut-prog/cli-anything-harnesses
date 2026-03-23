from setuptools import setup
setup(
    name='cli-anything-welcome',
    version='1.0.0',
    packages=['cli_anything.welcome'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-welcome=cli_anything.welcome:cli']},
)
