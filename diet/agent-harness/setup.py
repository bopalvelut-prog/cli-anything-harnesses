from setuptools import setup
setup(
    name='cli-anything-diet',
    version='1.0.0',
    packages=['cli_anything.diet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-diet=cli_anything.diet:cli']},
)
