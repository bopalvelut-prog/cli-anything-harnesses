from setuptools import setup
setup(
    name='cli-anything-value',
    version='1.0.0',
    packages=['cli_anything.value'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-value=cli_anything.value:cli']},
)
