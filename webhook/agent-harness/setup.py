from setuptools import setup
setup(
    name='cli-anything-webhook',
    version='1.0.0',
    packages=['cli_anything.webhook'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-webhook=cli_anything.webhook:cli']},
)
