from setuptools import setup
setup(
    name='cli-anything-secret',
    version='1.0.0',
    packages=['cli_anything.secret'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-secret=cli_anything.secret:cli']},
)
