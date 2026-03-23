from setuptools import setup
setup(
    name='cli-anything-replace',
    version='1.0.0',
    packages=['cli_anything.replace'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-replace=cli_anything.replace:cli']},
)
