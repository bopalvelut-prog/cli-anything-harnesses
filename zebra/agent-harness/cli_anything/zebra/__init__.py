import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zebra running')
@cli.command()
def start(): click.echo('zebra started')
if __name__ == '__main__': cli()
