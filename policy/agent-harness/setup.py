from setuptools import setup
setup(
    name='cli-anything-policy',
    version='1.0.0',
    packages=['cli_anything.policy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-policy=cli_anything.policy:cli']},
)
