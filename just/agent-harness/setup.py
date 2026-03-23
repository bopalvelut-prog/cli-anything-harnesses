from setuptools import setup
setup(
    name='cli-anything-just',
    version='1.0.0',
    packages=['cli_anything.just'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-just=cli_anything.just:cli']},
)
