from setuptools import setup
setup(
    name='cli-anything-every',
    version='1.0.0',
    packages=['cli_anything.every'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-every=cli_anything.every:cli']},
)
