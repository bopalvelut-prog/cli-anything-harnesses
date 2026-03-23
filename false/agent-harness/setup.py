from setuptools import setup
setup(
    name='cli-anything-false',
    version='1.0.0',
    packages=['cli_anything.false'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-false=cli_anything.false:cli']},
)
