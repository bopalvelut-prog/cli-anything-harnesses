from setuptools import setup
setup(
    name='cli-anything-timular',
    version='1.0.0',
    packages=['cli_anything.timular'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-timular=cli_anything.timular:cli']},
)
