from setuptools import setup
setup(
    name='cli-anything-freebsd',
    version='1.0.0',
    packages=['cli_anything.freebsd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-freebsd=cli_anything.freebsd:cli']},
)
