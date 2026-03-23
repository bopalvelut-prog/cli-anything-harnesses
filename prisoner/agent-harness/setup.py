from setuptools import setup
setup(
    name='cli-anything-prisoner',
    version='1.0.0',
    packages=['cli_anything.prisoner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prisoner=cli_anything.prisoner:cli']},
)
