from setuptools import setup
setup(
    name='cli-anything-most',
    version='1.0.0',
    packages=['cli_anything.most'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-most=cli_anything.most:cli']},
)
