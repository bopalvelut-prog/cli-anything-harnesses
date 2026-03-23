from setuptools import setup
setup(
    name='cli-anything-twenty',
    version='1.0.0',
    packages=['cli_anything.twenty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-twenty=cli_anything.twenty:cli']},
)
