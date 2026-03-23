import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('before running')
@cli.command()
def start(): click.echo('before started')
if __name__ == '__main__': cli()
