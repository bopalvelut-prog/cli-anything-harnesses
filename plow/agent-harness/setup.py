from setuptools import setup
setup(
    name='cli-anything-plow',
    version='1.0.0',
    packages=['cli_anything.plow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plow=cli_anything.plow:cli']},
)
