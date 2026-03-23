import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yugabytedb running')
@cli.command()
def start(): click.echo('yugabytedb started')
if __name__ == '__main__': cli()
