from setuptools import setup
setup(
    name='cli-anything-internal',
    version='1.0.0',
    packages=['cli_anything.internal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-internal=cli_anything.internal:cli']},
)
