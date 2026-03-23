from setuptools import setup
setup(
    name='cli-anything-wandb_v2',
    version='1.0.0',
    packages=['cli_anything.wandb_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wandb_v2=cli_anything.wandb_v2:cli']},
)
