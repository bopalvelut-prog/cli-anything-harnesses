from setuptools import setup
setup(
    name='cli-anything-withdraw',
    version='1.0.0',
    packages=['cli_anything.withdraw'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-withdraw=cli_anything.withdraw:cli']},
)
