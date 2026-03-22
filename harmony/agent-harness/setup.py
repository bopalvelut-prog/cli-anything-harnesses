from setuptools import setup
setup(
    name='cli-anything-harmony',
    version='1.0.0',
    packages=['cli_anything.harmony'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-harmony=cli_anything.harmony:cli']},
)
