from setuptools import setup
setup(
    name='cli-anything-spokesman',
    version='1.0.0',
    packages=['cli_anything.spokesman'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spokesman=cli_anything.spokesman:cli']},
)
