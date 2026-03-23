from setuptools import setup
setup(
    name='cli-anything-postmortem',
    version='1.0.0',
    packages=['cli_anything.postmortem'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-postmortem=cli_anything.postmortem:cli']},
)
