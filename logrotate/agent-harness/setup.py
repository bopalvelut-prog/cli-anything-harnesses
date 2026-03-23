from setuptools import setup
setup(
    name='cli-anything-logrotate',
    version='1.0.0',
    packages=['cli_anything.logrotate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-logrotate=cli_anything.logrotate:cli']},
)
