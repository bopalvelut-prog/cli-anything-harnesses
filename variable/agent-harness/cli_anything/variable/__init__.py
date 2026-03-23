import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('variable running')
@cli.command()
def start(): click.echo('variable started')
if __name__ == '__main__': cli()
