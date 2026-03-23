from setuptools import setup
setup(
    name='cli-anything-wedding',
    version='1.0.0',
    packages=['cli_anything.wedding'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wedding=cli_anything.wedding:cli']},
)
