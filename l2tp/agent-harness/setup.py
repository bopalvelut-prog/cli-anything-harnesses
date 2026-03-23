from setuptools import setup
setup(
    name='cli-anything-l2tp',
    version='1.0.0',
    packages=['cli_anything.l2tp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-l2tp=cli_anything.l2tp:cli']},
)
