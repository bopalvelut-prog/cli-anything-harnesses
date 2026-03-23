from setuptools import setup
setup(
    name='cli-anything-smpp',
    version='1.0.0',
    packages=['cli_anything.smpp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-smpp=cli_anything.smpp:cli']},
)
