import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cups running')
@cli.command()
def start(): click.echo('cups started')
if __name__ == '__main__': cli()
