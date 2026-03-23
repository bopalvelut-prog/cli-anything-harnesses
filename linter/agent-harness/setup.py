from setuptools import setup
setup(
    name='cli-anything-linter',
    version='1.0.0',
    packages=['cli_anything.linter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-linter=cli_anything.linter:cli']},
)
