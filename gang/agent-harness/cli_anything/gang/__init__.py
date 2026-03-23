import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gang running')
@cli.command()
def start(): click.echo('gang started')
if __name__ == '__main__': cli()
