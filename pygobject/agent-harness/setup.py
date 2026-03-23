from setuptools import setup
setup(
    name='cli-anything-pygobject',
    version='1.0.0',
    packages=['cli_anything.pygobject'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pygobject=cli_anything.pygobject:cli']},
)
