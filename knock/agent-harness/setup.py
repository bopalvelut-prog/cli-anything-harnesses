from setuptools import setup
setup(
    name='cli-anything-knock',
    version='1.0.0',
    packages=['cli_anything.knock'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-knock=cli_anything.knock:cli']},
)
