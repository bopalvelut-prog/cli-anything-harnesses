import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('timer running')
@cli.command()
def start(): click.echo('timer started')
if __name__ == '__main__': cli()
