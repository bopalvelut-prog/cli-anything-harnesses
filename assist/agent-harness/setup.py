from setuptools import setup
setup(
    name='cli-anything-assist',
    version='1.0.0',
    packages=['cli_anything.assist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-assist=cli_anything.assist:cli']},
)
