from setuptools import setup
setup(
    name='cli-anything-huggingface',
    version='1.0.0',
    packages=['cli_anything.huggingface'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-huggingface=cli_anything.huggingface:cli']},
)
