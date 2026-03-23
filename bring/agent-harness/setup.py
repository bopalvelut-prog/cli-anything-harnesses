from setuptools import setup
setup(
    name='cli-anything-bring',
    version='1.0.0',
    packages=['cli_anything.bring'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bring=cli_anything.bring:cli']},
)
