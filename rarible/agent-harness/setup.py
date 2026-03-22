from setuptools import setup
setup(
    name='cli-anything-rarible',
    version='1.0.0',
    packages=['cli_anything.rarible'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rarible=cli_anything.rarible:cli']},
)
