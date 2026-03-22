import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Sonarr status')
@cli.command()
def series(): click.echo('Series list')
if __name__ == '__main__': cli()
