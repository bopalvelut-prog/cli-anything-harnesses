from setuptools import setup
setup(
    name='cli-anything-caprover',
    version='1.0.0',
    packages=['cli_anything.caprover'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-caprover=cli_anything.caprover:cli']},
)
