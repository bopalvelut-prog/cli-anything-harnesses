from setuptools import setup
setup(
    name='cli-anything-emqtt',
    version='1.0.0',
    packages=['cli_anything.emqtt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-emqtt=cli_anything.emqtt:cli']},
)
