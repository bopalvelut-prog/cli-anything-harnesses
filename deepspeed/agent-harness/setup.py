from setuptools import setup
setup(
    name='cli-anything-deepspeed',
    version='1.0.0',
    packages=['cli_anything.deepspeed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deepspeed=cli_anything.deepspeed:cli']},
)
