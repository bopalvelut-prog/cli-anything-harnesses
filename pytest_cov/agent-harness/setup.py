from setuptools import setup
setup(
    name='cli-anything-pytest_cov',
    version='1.0.0',
    packages=['cli_anything.pytest_cov'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pytest_cov=cli_anything.pytest_cov:cli']},
)
