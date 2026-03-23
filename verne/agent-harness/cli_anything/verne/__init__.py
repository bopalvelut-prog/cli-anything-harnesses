import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('verne running')
@cli.command()
def start(): click.echo('verne started')
if __name__ == '__main__': cli()
