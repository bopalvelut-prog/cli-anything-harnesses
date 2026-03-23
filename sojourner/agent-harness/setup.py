from setuptools import setup
setup(
    name='cli-anything-sojourner',
    version='1.0.0',
    packages=['cli_anything.sojourner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sojourner=cli_anything.sojourner:cli']},
)
