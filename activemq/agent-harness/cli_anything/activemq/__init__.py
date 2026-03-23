import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('activemq running')
@cli.command()
def start(): click.echo('activemq started')
if __name__ == '__main__': cli()
