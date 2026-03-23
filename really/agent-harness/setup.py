from setuptools import setup
setup(
    name='cli-anything-really',
    version='1.0.0',
    packages=['cli_anything.really'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-really=cli_anything.really:cli']},
)
