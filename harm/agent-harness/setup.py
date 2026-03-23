from setuptools import setup
setup(
    name='cli-anything-harm',
    version='1.0.0',
    packages=['cli_anything.harm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-harm=cli_anything.harm:cli']},
)
