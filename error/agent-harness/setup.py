from setuptools import setup
setup(
    name='cli-anything-error',
    version='1.0.0',
    packages=['cli_anything.error'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-error=cli_anything.error:cli']},
)
