import click
@click.group()
def cli(): pass
@cli.command()
def generate(): click.echo('Pika generate')
@cli.command()
def list(): click.echo('Pika list')
if __name__ == '__main__': cli()
