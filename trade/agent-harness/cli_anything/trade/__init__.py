import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trade running')
@cli.command()
def start(): click.echo('trade started')
if __name__ == '__main__': cli()
