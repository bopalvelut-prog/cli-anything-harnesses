import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rail running')
@cli.command()
def start(): click.echo('rail started')
if __name__ == '__main__': cli()
