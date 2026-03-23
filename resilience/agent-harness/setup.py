from setuptools import setup
setup(
    name='cli-anything-resilience',
    version='1.0.0',
    packages=['cli_anything.resilience'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-resilience=cli_anything.resilience:cli']},
)
