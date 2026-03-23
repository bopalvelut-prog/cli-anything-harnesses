import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hurry running')
@cli.command()
def start(): click.echo('hurry started')
if __name__ == '__main__': cli()
