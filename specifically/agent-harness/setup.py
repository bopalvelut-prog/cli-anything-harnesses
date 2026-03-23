from setuptools import setup
setup(
    name='cli-anything-specifically',
    version='1.0.0',
    packages=['cli_anything.specifically'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-specifically=cli_anything.specifically:cli']},
)
