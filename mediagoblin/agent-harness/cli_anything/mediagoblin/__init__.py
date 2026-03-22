import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('MediaGoblin status')
@cli.command()
def media(): click.echo('MediaGoblin media')
if __name__ == '__main__': cli()
