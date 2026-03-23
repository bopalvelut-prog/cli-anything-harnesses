from setuptools import setup
setup(
    name='cli-anything-retirement',
    version='1.0.0',
    packages=['cli_anything.retirement'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-retirement=cli_anything.retirement:cli']},
)
