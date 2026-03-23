from setuptools import setup
setup(
    name='cli-anything-redash',
    version='1.0.0',
    packages=['cli_anything.redash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-redash=cli_anything.redash:cli']},
)
