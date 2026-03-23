from setuptools import setup
setup(
    name='cli-anything-kbfs',
    version='1.0.0',
    packages=['cli_anything.kbfs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kbfs=cli_anything.kbfs:cli']},
)
