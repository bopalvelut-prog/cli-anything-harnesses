from setuptools import setup
setup(
    name='cli-anything-pytorch_lightning',
    version='1.0.0',
    packages=['cli_anything.pytorch_lightning'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pytorch_lightning=cli_anything.pytorch_lightning:cli']},
)
