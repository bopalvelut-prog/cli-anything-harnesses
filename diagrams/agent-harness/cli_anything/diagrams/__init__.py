import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('diagrams running')
@cli.command()
def start(): click.echo('diagrams started')
if __name__ == '__main__': cli()
