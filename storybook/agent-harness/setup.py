from setuptools import setup
setup(
    name='cli-anything-storybook',
    version='1.0.0',
    packages=['cli_anything.storybook'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-storybook=cli_anything.storybook:cli']},
)
