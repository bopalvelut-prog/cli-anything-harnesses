from setuptools import setup
setup(
    name='cli-anything-aave',
    version='1.0.0',
    packages=['cli_anything.aave'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aave=cli_anything.aave:cli']},
)
