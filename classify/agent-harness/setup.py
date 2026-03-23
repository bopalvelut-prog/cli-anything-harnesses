from setuptools import setup
setup(
    name='cli-anything-classify',
    version='1.0.0',
    packages=['cli_anything.classify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-classify=cli_anything.classify:cli']},
)
