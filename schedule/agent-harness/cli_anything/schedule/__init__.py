import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('schedule running')
@cli.command()
def start(): click.echo('schedule started')
if __name__ == '__main__': cli()
