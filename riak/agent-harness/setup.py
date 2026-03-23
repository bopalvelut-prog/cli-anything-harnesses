from setuptools import setup
setup(
    name='cli-anything-riak',
    version='1.0.0',
    packages=['cli_anything.riak'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-riak=cli_anything.riak:cli']},
)
