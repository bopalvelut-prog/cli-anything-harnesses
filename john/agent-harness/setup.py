from setuptools import setup
setup(
    name='cli-anything-john',
    version='1.0.0',
    packages=['cli_anything.john'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-john=cli_anything.john:cli']},
)
