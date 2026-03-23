import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('software running')
@cli.command()
def start(): click.echo('software started')
if __name__ == '__main__': cli()
