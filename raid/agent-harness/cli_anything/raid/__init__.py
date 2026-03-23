import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('raid running')
@cli.command()
def start(): click.echo('raid started')
if __name__ == '__main__': cli()
