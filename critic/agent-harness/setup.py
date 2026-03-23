from setuptools import setup
setup(
    name='cli-anything-critic',
    version='1.0.0',
    packages=['cli_anything.critic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-critic=cli_anything.critic:cli']},
)
