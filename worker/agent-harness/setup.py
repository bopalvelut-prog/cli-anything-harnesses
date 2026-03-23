from setuptools import setup
setup(
    name='cli-anything-worker',
    version='1.0.0',
    packages=['cli_anything.worker'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-worker=cli_anything.worker:cli']},
)
