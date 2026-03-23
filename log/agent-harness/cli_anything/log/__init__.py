import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('log running')
@cli.command()
def start(): click.echo('log started')
if __name__ == '__main__': cli()
