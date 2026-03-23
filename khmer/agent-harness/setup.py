from setuptools import setup
setup(
    name='cli-anything-khmer',
    version='1.0.0',
    packages=['cli_anything.khmer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-khmer=cli_anything.khmer:cli']},
)
