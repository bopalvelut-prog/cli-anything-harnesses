from setuptools import setup
setup(
    name='cli-anything-boom',
    version='1.0.0',
    packages=['cli_anything.boom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-boom=cli_anything.boom:cli']},
)
