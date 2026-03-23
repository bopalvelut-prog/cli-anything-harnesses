from setuptools import setup
setup(
    name='cli-anything-reward',
    version='1.0.0',
    packages=['cli_anything.reward'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reward=cli_anything.reward:cli']},
)
