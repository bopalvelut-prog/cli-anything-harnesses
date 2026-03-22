from setuptools import setup
setup(
    name='cli-anything-livechat',
    version='1.0.0',
    packages=['cli_anything.livechat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-livechat=cli_anything.livechat:cli']},
)
