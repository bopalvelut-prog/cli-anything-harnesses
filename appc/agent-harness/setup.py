from setuptools import setup
setup(
    name='cli-anything-appc',
    version='1.0.0',
    packages=['cli_anything.appc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-appc=cli_anything.appc:cli']},
)
