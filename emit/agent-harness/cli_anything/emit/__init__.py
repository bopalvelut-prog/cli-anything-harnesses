import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('emit running')
@cli.command()
def start(): click.echo('emit started')
if __name__ == '__main__': cli()
