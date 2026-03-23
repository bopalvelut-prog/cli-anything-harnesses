from setuptools import setup
setup(
    name='cli-anything-propose',
    version='1.0.0',
    packages=['cli_anything.propose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-propose=cli_anything.propose:cli']},
)
