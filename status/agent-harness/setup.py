from setuptools import setup
setup(
    name='cli-anything-status',
    version='1.0.0',
    packages=['cli_anything.status'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-status=cli_anything.status:cli']},
)
