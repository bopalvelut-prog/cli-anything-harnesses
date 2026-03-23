from setuptools import setup
setup(
    name='cli-anything-semaphore',
    version='1.0.0',
    packages=['cli_anything.semaphore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-semaphore=cli_anything.semaphore:cli']},
)
