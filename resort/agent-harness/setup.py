from setuptools import setup
setup(
    name='cli-anything-resort',
    version='1.0.0',
    packages=['cli_anything.resort'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-resort=cli_anything.resort:cli']},
)
