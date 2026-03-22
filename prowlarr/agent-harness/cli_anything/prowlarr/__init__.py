import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Prowlarr status')
@cli.command()
def indexers(): click.echo('Indexers list')
if __name__ == '__main__': cli()
