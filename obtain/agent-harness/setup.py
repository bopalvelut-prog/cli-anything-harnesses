from setuptools import setup
setup(
    name='cli-anything-obtain',
    version='1.0.0',
    packages=['cli_anything.obtain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-obtain=cli_anything.obtain:cli']},
)
