import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('disc running')
@cli.command()
def start(): click.echo('disc started')
if __name__ == '__main__': cli()
