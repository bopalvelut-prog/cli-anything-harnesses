import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ugly running')
@cli.command()
def start(): click.echo('ugly started')
if __name__ == '__main__': cli()
