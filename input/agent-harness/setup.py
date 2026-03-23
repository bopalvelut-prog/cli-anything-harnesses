from setuptools import setup
setup(
    name='cli-anything-input',
    version='1.0.0',
    packages=['cli_anything.input'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-input=cli_anything.input:cli']},
)
