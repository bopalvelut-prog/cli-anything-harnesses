from setuptools import setup
setup(
    name='cli-anything-retry',
    version='1.0.0',
    packages=['cli_anything.retry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-retry=cli_anything.retry:cli']},
)
