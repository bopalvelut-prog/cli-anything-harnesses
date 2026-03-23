from setuptools import setup
setup(
    name='cli-anything-runtime',
    version='1.0.0',
    packages=['cli_anything.runtime'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-runtime=cli_anything.runtime:cli']},
)
