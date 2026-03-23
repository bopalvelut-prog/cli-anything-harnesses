import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bronze running')
@cli.command()
def start(): click.echo('bronze started')
if __name__ == '__main__': cli()
