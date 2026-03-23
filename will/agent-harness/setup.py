from setuptools import setup
setup(
    name='cli-anything-will',
    version='1.0.0',
    packages=['cli_anything.will'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-will=cli_anything.will:cli']},
)
