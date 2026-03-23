import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('last running')
@cli.command()
def start(): click.echo('last started')
if __name__ == '__main__': cli()
