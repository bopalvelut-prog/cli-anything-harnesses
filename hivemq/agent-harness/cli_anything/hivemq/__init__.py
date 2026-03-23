import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hivemq running')
@cli.command()
def start(): click.echo('hivemq started')
if __name__ == '__main__': cli()
