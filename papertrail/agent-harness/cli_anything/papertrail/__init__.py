import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('papertrail running')
@cli.command()
def start(): click.echo('papertrail started')
if __name__ == '__main__': cli()
