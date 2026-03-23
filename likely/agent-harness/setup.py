from setuptools import setup
setup(
    name='cli-anything-likely',
    version='1.0.0',
    packages=['cli_anything.likely'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-likely=cli_anything.likely:cli']},
)
