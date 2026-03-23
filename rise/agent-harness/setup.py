from setuptools import setup
setup(
    name='cli-anything-rise',
    version='1.0.0',
    packages=['cli_anything.rise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rise=cli_anything.rise:cli']},
)
