import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('profession running')
@cli.command()
def start(): click.echo('profession started')
if __name__ == '__main__': cli()
