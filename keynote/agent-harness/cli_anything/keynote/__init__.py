import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('keynote running')
@cli.command()
def start(): click.echo('keynote started')
if __name__ == '__main__': cli()
