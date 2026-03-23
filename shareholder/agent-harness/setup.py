from setuptools import setup
setup(
    name='cli-anything-shareholder',
    version='1.0.0',
    packages=['cli_anything.shareholder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shareholder=cli_anything.shareholder:cli']},
)
