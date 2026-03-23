from setuptools import setup
setup(
    name='cli-anything-cohere',
    version='1.0.0',
    packages=['cli_anything.cohere'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cohere=cli_anything.cohere:cli']},
)
