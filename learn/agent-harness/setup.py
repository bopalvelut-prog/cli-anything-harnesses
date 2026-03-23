from setuptools import setup
setup(
    name='cli-anything-learn',
    version='1.0.0',
    packages=['cli_anything.learn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-learn=cli_anything.learn:cli']},
)
