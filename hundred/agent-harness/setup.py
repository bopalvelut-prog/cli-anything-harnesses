from setuptools import setup
setup(
    name='cli-anything-hundred',
    version='1.0.0',
    packages=['cli_anything.hundred'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hundred=cli_anything.hundred:cli']},
)
