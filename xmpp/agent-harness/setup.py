from setuptools import setup
setup(
    name='cli-anything-xmpp',
    version='1.0.0',
    packages=['cli_anything.xmpp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xmpp=cli_anything.xmpp:cli']},
)
