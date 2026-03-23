import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('debt running')
@cli.command()
def start(): click.echo('debt started')
if __name__ == '__main__': cli()
