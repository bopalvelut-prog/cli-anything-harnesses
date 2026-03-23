from setuptools import setup
setup(
    name='cli-anything-messaging',
    version='1.0.0',
    packages=['cli_anything.messaging'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-messaging=cli_anything.messaging:cli']},
)
