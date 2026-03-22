from setuptools import setup
setup(
    name='cli-anything-lint',
    version='1.0.0',
    packages=['cli_anything.lint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lint=cli_anything.lint:cli']},
)
