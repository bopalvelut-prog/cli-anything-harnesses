from setuptools import setup
setup(
    name='cli-anything-stepping',
    version='1.0.0',
    packages=['cli_anything.stepping'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stepping=cli_anything.stepping:cli']},
)
