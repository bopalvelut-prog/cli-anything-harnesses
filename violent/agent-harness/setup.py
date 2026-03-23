from setuptools import setup
setup(
    name='cli-anything-violent',
    version='1.0.0',
    packages=['cli_anything.violent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-violent=cli_anything.violent:cli']},
)
