from setuptools import setup
setup(
    name='cli-anything-expect',
    version='1.0.0',
    packages=['cli_anything.expect'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-expect=cli_anything.expect:cli']},
)
