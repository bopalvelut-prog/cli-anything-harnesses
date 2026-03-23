from setuptools import setup
setup(
    name='cli-anything-proportion',
    version='1.0.0',
    packages=['cli_anything.proportion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-proportion=cli_anything.proportion:cli']},
)
