import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('statement running')
@cli.command()
def start(): click.echo('statement started')
if __name__ == '__main__': cli()
