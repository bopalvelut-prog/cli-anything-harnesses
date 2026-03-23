from setuptools import setup
setup(
    name='cli-anything-batch',
    version='1.0.0',
    packages=['cli_anything.batch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-batch=cli_anything.batch:cli']},
)
