import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flower running')
@cli.command()
def start(): click.echo('flower started')
if __name__ == '__main__': cli()
