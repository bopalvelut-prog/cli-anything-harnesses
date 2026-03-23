from setuptools import setup
setup(
    name='cli-anything-weekly',
    version='1.0.0',
    packages=['cli_anything.weekly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weekly=cli_anything.weekly:cli']},
)
