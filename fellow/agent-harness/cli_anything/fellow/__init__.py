import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fellow running')
@cli.command()
def start(): click.echo('fellow started')
if __name__ == '__main__': cli()
