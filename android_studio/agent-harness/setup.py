from setuptools import setup
setup(
    name='cli-anything-android_studio',
    version='1.0.0',
    packages=['cli_anything.android_studio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-android_studio=cli_anything.android_studio:cli']},
)
