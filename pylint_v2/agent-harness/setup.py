from setuptools import setup
setup(
    name='cli-anything-pylint_v2',
    version='1.0.0',
    packages=['cli_anything.pylint_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pylint_v2=cli_anything.pylint_v2:cli']},
)
