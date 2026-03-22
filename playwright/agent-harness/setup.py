from setuptools import setup
setup(
    name='cli-anything-playwright',
    version='1.0.0',
    packages=['cli_anything.playwright'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-playwright=cli_anything.playwright:cli']},
)
