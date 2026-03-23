import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('consider running')
@cli.command()
def start(): click.echo('consider started')
if __name__ == '__main__': cli()
