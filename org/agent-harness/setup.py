from setuptools import setup
setup(
    name='cli-anything-org',
    version='1.0.0',
    packages=['cli_anything.org'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-org=cli_anything.org:cli']},
)
