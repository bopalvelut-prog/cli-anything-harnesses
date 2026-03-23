from setuptools import setup
setup(
    name='cli-anything-aria',
    version='1.0.0',
    packages=['cli_anything.aria'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aria=cli_anything.aria:cli']},
)
