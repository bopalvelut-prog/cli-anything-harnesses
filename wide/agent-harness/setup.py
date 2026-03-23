from setuptools import setup
setup(
    name='cli-anything-wide',
    version='1.0.0',
    packages=['cli_anything.wide'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wide=cli_anything.wide:cli']},
)
