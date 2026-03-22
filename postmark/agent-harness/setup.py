from setuptools import setup
setup(
    name='cli-anything-postmark',
    version='1.0.0',
    packages=['cli_anything.postmark'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-postmark=cli_anything.postmark:cli']},
)
