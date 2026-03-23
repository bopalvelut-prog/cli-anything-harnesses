from setuptools import setup
setup(
    name='cli-anything-mayor',
    version='1.0.0',
    packages=['cli_anything.mayor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mayor=cli_anything.mayor:cli']},
)
