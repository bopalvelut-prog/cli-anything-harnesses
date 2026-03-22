from setuptools import setup
setup(
    name='cli-anything-prettier',
    version='1.0.0',
    packages=['cli_anything.prettier'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prettier=cli_anything.prettier:cli']},
)
