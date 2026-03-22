import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Radarr status')
@cli.command()
def movies(): click.echo('Movies list')
if __name__ == '__main__': cli()
