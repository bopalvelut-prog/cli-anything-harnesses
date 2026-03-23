from setuptools import setup
setup(
    name='cli-anything-pinot',
    version='1.0.0',
    packages=['cli_anything.pinot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pinot=cli_anything.pinot:cli']},
)
