from setuptools import setup
setup(
    name='cli-anything-mastodon',
    version='1.0.0',
    packages=['cli_anything.mastodon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mastodon=cli_anything.mastodon:cli']},
)
