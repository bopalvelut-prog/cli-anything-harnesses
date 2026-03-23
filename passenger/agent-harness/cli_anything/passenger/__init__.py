import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('passenger running')
@cli.command()
def start(): click.echo('passenger started')
if __name__ == '__main__': cli()
