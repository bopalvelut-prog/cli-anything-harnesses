import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('application running')
@cli.command()
def start(): click.echo('application started')
if __name__ == '__main__': cli()
