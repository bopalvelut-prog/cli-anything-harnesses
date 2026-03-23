from setuptools import setup
setup(
    name='cli-anything-cattrs',
    version='1.0.0',
    packages=['cli_anything.cattrs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cattrs=cli_anything.cattrs:cli']},
)
