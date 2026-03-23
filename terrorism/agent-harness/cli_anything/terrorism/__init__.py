import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('terrorism running')
@cli.command()
def start(): click.echo('terrorism started')
if __name__ == '__main__': cli()
