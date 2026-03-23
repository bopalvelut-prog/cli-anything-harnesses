import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bring running')
@cli.command()
def start(): click.echo('bring started')
if __name__ == '__main__': cli()
