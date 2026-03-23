from setuptools import setup
setup(
    name='cli-anything-actionhero',
    version='1.0.0',
    packages=['cli_anything.actionhero'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-actionhero=cli_anything.actionhero:cli']},
)
