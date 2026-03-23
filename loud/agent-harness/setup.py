from setuptools import setup
setup(
    name='cli-anything-loud',
    version='1.0.0',
    packages=['cli_anything.loud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-loud=cli_anything.loud:cli']},
)
