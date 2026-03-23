import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('horse running')
@cli.command()
def start(): click.echo('horse started')
if __name__ == '__main__': cli()
