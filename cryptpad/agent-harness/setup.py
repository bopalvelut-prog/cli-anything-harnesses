from setuptools import setup
setup(
    name='cli-anything-cryptpad',
    version='1.0.0',
    packages=['cli_anything.cryptpad'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cryptpad=cli_anything.cryptpad:cli']},
)
