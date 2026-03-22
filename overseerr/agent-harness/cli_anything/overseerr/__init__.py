import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Overseerr status')
@cli.command()
def requests(): click.echo('Requests list')
if __name__ == '__main__': cli()
