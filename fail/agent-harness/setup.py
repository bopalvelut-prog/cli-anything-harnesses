from setuptools import setup
setup(
    name='cli-anything-fail',
    version='1.0.0',
    packages=['cli_anything.fail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fail=cli_anything.fail:cli']},
)
