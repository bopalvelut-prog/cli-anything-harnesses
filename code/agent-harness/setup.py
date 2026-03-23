from setuptools import setup
setup(
    name='cli-anything-code',
    version='1.0.0',
    packages=['cli_anything.code'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-code=cli_anything.code:cli']},
)
