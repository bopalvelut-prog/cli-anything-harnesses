from setuptools import setup
setup(
    name='cli-anything-brother',
    version='1.0.0',
    packages=['cli_anything.brother'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brother=cli_anything.brother:cli']},
)
