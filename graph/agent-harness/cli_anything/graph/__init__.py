import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('graph running')
@cli.command()
def start(): click.echo('graph started')
if __name__ == '__main__': cli()
