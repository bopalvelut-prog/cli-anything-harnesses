from setuptools import setup
setup(
    name='cli-anything-timeout',
    version='1.0.0',
    packages=['cli_anything.timeout'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-timeout=cli_anything.timeout:cli']},
)
