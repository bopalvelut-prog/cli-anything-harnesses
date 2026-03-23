import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autocannon running')
@cli.command()
def start(): click.echo('autocannon started')
if __name__ == '__main__': cli()
