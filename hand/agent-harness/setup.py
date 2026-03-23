from setuptools import setup
setup(
    name='cli-anything-hand',
    version='1.0.0',
    packages=['cli_anything.hand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hand=cli_anything.hand:cli']},
)
