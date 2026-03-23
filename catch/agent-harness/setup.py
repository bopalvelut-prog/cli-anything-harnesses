from setuptools import setup
setup(
    name='cli-anything-catch',
    version='1.0.0',
    packages=['cli_anything.catch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-catch=cli_anything.catch:cli']},
)
