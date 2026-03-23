import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('couple running')
@cli.command()
def start(): click.echo('couple started')
if __name__ == '__main__': cli()
