from setuptools import setup
setup(
    name='cli-anything-amazon',
    version='1.0.0',
    packages=['cli_anything.amazon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon=cli_anything.amazon:cli']},
)
