import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bow running')
@cli.command()
def start(): click.echo('bow started')
if __name__ == '__main__': cli()
