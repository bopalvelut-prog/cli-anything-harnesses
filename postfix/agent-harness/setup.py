from setuptools import setup
setup(
    name='cli-anything-postfix',
    version='1.0.0',
    packages=['cli_anything.postfix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-postfix=cli_anything.postfix:cli']},
)
