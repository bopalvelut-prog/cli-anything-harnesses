import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('framework running')
@cli.command()
def start(): click.echo('framework started')
if __name__ == '__main__': cli()
