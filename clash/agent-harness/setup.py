from setuptools import setup
setup(
    name='cli-anything-clash',
    version='1.0.0',
    packages=['cli_anything.clash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clash=cli_anything.clash:cli']},
)
