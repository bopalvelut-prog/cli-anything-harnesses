from setuptools import setup
setup(
    name='cli-anything-withdrawal',
    version='1.0.0',
    packages=['cli_anything.withdrawal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-withdrawal=cli_anything.withdrawal:cli']},
)
