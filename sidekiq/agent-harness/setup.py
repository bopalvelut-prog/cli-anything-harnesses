from setuptools import setup
setup(
    name='cli-anything-sidekiq',
    version='1.0.0',
    packages=['cli_anything.sidekiq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sidekiq=cli_anything.sidekiq:cli']},
)
