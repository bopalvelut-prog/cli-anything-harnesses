from setuptools import setup
setup(
    name='cli-anything-breath',
    version='1.0.0',
    packages=['cli_anything.breath'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-breath=cli_anything.breath:cli']},
)
