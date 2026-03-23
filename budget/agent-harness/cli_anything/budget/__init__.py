import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('budget running')
@cli.command()
def start(): click.echo('budget started')
if __name__ == '__main__': cli()
