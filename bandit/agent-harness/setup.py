from setuptools import setup
setup(
    name='cli-anything-bandit',
    version='1.0.0',
    packages=['cli_anything.bandit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bandit=cli_anything.bandit:cli']},
)
