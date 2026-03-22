from setuptools import setup
setup(
    name='cli-anything-wandb',
    version='1.0.0',
    packages=['cli_anything.wandb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wandb=cli_anything.wandb:cli']},
)
