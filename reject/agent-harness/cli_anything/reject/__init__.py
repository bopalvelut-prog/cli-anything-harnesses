import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reject running')
@cli.command()
def start(): click.echo('reject started')
if __name__ == '__main__': cli()
