import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('medium running')
@cli.command()
def start(): click.echo('medium started')
if __name__ == '__main__': cli()
