from setuptools import setup
setup(
    name='cli-anything-month',
    version='1.0.0',
    packages=['cli_anything.month'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-month=cli_anything.month:cli']},
)
