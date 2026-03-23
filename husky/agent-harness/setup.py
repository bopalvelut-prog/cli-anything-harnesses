from setuptools import setup
setup(
    name='cli-anything-husky',
    version='1.0.0',
    packages=['cli_anything.husky'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-husky=cli_anything.husky:cli']},
)
