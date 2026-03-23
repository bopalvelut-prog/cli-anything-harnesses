import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mortgage running')
@cli.command()
def start(): click.echo('mortgage started')
if __name__ == '__main__': cli()
