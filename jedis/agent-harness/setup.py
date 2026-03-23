from setuptools import setup
setup(
    name='cli-anything-jedis',
    version='1.0.0',
    packages=['cli_anything.jedis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jedis=cli_anything.jedis:cli']},
)
