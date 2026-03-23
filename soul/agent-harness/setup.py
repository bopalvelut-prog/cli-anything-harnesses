from setuptools import setup
setup(
    name='cli-anything-soul',
    version='1.0.0',
    packages=['cli_anything.soul'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-soul=cli_anything.soul:cli']},
)
