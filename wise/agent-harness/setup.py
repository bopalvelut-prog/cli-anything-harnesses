from setuptools import setup
setup(
    name='cli-anything-wise',
    version='1.0.0',
    packages=['cli_anything.wise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wise=cli_anything.wise:cli']},
)
