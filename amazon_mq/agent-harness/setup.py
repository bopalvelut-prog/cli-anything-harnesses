from setuptools import setup
setup(
    name='cli-anything-amazon_mq',
    version='1.0.0',
    packages=['cli_anything.amazon_mq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_mq=cli_anything.amazon_mq:cli']},
)
