from setuptools import setup
setup(
    name='cli-anything-method',
    version='1.0.0',
    packages=['cli_anything.method'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-method=cli_anything.method:cli']},
)
