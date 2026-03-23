import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('transaction running')
@cli.command()
def start(): click.echo('transaction started')
if __name__ == '__main__': cli()
