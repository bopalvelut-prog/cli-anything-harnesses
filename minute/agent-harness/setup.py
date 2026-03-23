from setuptools import setup
setup(
    name='cli-anything-minute',
    version='1.0.0',
    packages=['cli_anything.minute'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-minute=cli_anything.minute:cli']},
)
