from setuptools import setup
setup(
    name='cli-anything-cron',
    version='1.0.0',
    packages=['cli_anything.cron'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cron=cli_anything.cron:cli']},
)
