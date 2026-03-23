import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('staff running')
@cli.command()
def start(): click.echo('staff started')
if __name__ == '__main__': cli()
