from setuptools import setup
setup(
    name='cli-anything-return',
    version='1.0.0',
    packages=['cli_anything.return'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-return=cli_anything.return:cli']},
)
