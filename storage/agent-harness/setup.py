from setuptools import setup
setup(
    name='cli-anything-storage',
    version='1.0.0',
    packages=['cli_anything.storage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-storage=cli_anything.storage:cli']},
)
