from setuptools import setup
setup(
    name='cli-anything-multiprocessing',
    version='1.0.0',
    packages=['cli_anything.multiprocessing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-multiprocessing=cli_anything.multiprocessing:cli']},
)
