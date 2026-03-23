from setuptools import setup
setup(
    name='cli-anything-cool',
    version='1.0.0',
    packages=['cli_anything.cool'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cool=cli_anything.cool:cli']},
)
