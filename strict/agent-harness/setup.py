from setuptools import setup
setup(
    name='cli-anything-strict',
    version='1.0.0',
    packages=['cli_anything.strict'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strict=cli_anything.strict:cli']},
)
