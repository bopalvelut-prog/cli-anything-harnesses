import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('asynquence running')
@cli.command()
def start(): click.echo('asynquence started')
if __name__ == '__main__': cli()
