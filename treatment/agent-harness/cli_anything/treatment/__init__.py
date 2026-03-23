import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('treatment running')
@cli.command()
def start(): click.echo('treatment started')
if __name__ == '__main__': cli()
