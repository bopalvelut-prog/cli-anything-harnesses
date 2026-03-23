import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('attack running')
@cli.command()
def start(): click.echo('attack started')
if __name__ == '__main__': cli()
