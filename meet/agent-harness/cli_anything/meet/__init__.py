import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('meet running')
@cli.command()
def start(): click.echo('meet started')
if __name__ == '__main__': cli()
