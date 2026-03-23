from setuptools import setup
setup(
    name='cli-anything-familiar',
    version='1.0.0',
    packages=['cli_anything.familiar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-familiar=cli_anything.familiar:cli']},
)
