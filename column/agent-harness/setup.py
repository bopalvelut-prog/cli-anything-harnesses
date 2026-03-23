from setuptools import setup
setup(
    name='cli-anything-column',
    version='1.0.0',
    packages=['cli_anything.column'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-column=cli_anything.column:cli']},
)
