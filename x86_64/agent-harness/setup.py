from setuptools import setup
setup(
    name='cli-anything-x86_64',
    version='1.0.0',
    packages=['cli_anything.x86_64'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-x86_64=cli_anything.x86_64:cli']},
)
