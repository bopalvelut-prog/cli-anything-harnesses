from setuptools import setup
setup(
    name='cli-anything-successful',
    version='1.0.0',
    packages=['cli_anything.successful'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-successful=cli_anything.successful:cli']},
)
