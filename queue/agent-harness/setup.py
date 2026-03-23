from setuptools import setup
setup(
    name='cli-anything-queue',
    version='1.0.0',
    packages=['cli_anything.queue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-queue=cli_anything.queue:cli']},
)
