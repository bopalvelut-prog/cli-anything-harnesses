from setuptools import setup
setup(
    name='cli-anything-retries',
    version='1.0.0',
    packages=['cli_anything.retries'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-retries=cli_anything.retries:cli']},
)
