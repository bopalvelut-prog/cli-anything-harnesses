from setuptools import setup
setup(
    name='cli-anything-okx',
    version='1.0.0',
    packages=['cli_anything.okx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-okx=cli_anything.okx:cli']},
)
