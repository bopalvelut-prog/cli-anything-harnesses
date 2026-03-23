from setuptools import setup
setup(
    name='cli-anything-jeans',
    version='1.0.0',
    packages=['cli_anything.jeans'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jeans=cli_anything.jeans:cli']},
)
