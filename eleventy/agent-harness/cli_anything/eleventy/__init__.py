import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): subprocess.run(['npx', '@11ty/eleventy', '--serve'])
@cli.command()
def build(): subprocess.run(['npx', '@11ty/eleventy'])
@cli.command()
def watch(): subprocess.run(['npx', '@11ty/eleventy', '--watch'])
if __name__ == '__main__': cli()
