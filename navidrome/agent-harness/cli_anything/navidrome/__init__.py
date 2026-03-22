import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Navidrome status')
@cli.command()
def artists(): click.echo('Artists list')
if __name__ == '__main__': cli()
