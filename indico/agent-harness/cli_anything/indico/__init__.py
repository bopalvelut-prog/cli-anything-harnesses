import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('indico running')
@cli.command()
def start(): click.echo('indico started')
if __name__ == '__main__': cli()
