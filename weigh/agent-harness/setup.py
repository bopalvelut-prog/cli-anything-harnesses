from setuptools import setup
setup(
    name='cli-anything-weigh',
    version='1.0.0',
    packages=['cli_anything.weigh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weigh=cli_anything.weigh:cli']},
)
