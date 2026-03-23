import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('something running')
@cli.command()
def start(): click.echo('something started')
if __name__ == '__main__': cli()
