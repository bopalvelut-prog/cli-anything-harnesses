from setuptools import setup
setup(
    name='cli-anything-amazon_q',
    version='1.0.0',
    packages=['cli_anything.amazon_q'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amazon_q=cli_anything.amazon_q:cli']},
)
