from setuptools import setup
setup(
    name='cli-anything-vote',
    version='1.0.0',
    packages=['cli_anything.vote'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vote=cli_anything.vote:cli']},
)
