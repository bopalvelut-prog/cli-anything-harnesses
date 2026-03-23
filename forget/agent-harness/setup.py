from setuptools import setup
setup(
    name='cli-anything-forget',
    version='1.0.0',
    packages=['cli_anything.forget'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-forget=cli_anything.forget:cli']},
)
