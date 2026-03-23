from setuptools import setup
setup(
    name='cli-anything-result',
    version='1.0.0',
    packages=['cli_anything.result'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-result=cli_anything.result:cli']},
)
