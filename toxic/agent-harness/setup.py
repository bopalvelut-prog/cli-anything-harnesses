from setuptools import setup
setup(
    name='cli-anything-toxic',
    version='1.0.0',
    packages=['cli_anything.toxic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-toxic=cli_anything.toxic:cli']},
)
