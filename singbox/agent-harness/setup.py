from setuptools import setup
setup(
    name='cli-anything-singbox',
    version='1.0.0',
    packages=['cli_anything.singbox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-singbox=cli_anything.singbox:cli']},
)
