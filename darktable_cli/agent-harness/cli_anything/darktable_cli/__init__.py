import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('input')
@click.argument('output')
def export(input, output): subprocess.run(['darktable-cli', input, output])
@cli.command()
def presets(): click.echo('Available presets')
if __name__ == '__main__': cli()
