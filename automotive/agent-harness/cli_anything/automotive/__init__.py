import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('automotive running')
@cli.command()
def start(): click.echo('automotive started')
if __name__ == '__main__': cli()
