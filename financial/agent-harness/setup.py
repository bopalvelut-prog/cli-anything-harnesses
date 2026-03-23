from setuptools import setup
setup(
    name='cli-anything-financial',
    version='1.0.0',
    packages=['cli_anything.financial'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-financial=cli_anything.financial:cli']},
)
