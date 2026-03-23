from setuptools import setup
setup(
    name='cli-anything-mystery',
    version='1.0.0',
    packages=['cli_anything.mystery'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mystery=cli_anything.mystery:cli']},
)
