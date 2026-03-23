from setuptools import setup
setup(
    name='cli-anything-join',
    version='1.0.0',
    packages=['cli_anything.join'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-join=cli_anything.join:cli']},
)
