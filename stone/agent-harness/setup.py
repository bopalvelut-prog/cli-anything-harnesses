from setuptools import setup
setup(
    name='cli-anything-stone',
    version='1.0.0',
    packages=['cli_anything.stone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stone=cli_anything.stone:cli']},
)
