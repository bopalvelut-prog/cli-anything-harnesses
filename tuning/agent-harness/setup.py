from setuptools import setup
setup(
    name='cli-anything-tuning',
    version='1.0.0',
    packages=['cli_anything.tuning'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tuning=cli_anything.tuning:cli']},
)
