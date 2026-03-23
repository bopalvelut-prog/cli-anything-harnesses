from setuptools import setup
setup(
    name='cli-anything-btrace',
    version='1.0.0',
    packages=['cli_anything.btrace'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-btrace=cli_anything.btrace:cli']},
)
