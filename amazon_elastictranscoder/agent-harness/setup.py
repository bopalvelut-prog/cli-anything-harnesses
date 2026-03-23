from setuptools import setup
setup(
    name='cli-anything-amazon_elastictranscoder',
    version='1.0.0',
    packages=['cli_anything.amazon_elastictranscoder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_elastictranscoder=cli_anything.amazon_elastictranscoder:cli']},
)
