import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('glassfish running')
@cli.command()
def start(): click.echo('glassfish started')
if __name__ == '__main__': cli()
